import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn

# ── Args ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--new-data", default="data/current.csv",
                    help="CSV to retrain on (default: data/current.csv)")
args = parser.parse_args()

print(f"🔁 Retraining on: {args.new_data}\n")

os.makedirs("models", exist_ok=True)
mlflow.set_experiment("Churn Retraining")


# ── Preprocessing (mirrors train.py exactly) ───────────────────────────────────
def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop(columns=["customerID"], errors="ignore")

    for col in df.select_dtypes(include="object").columns:
        if col == "Churn":
            continue
        coerced = pd.to_numeric(df[col], errors="coerce")
        if coerced.notna().mean() > 0.8:
            df[col] = coerced

    df = df.dropna()
    df["Churn"] = (df["Churn"].astype(str).str.strip().str.lower()
                   .isin(["yes", "1", "true"])).astype(int)
    df = pd.get_dummies(df)
    return df


df = preprocess(pd.read_csv(args.new_data))

X = df.drop(columns=["Churn"])
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

N_ESTIMATORS = 50

with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"New Accuracy: {acc:.4f}")

    mlflow.log_param("n_estimators", N_ESTIMATORS)
    mlflow.log_param("retrain_source", args.new_data)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

    existing   = [f for f in os.listdir("models") if f.startswith("model_v")]
    version    = len(existing) + 1
    model_path = f"models/model_v{version}.pkl"
    joblib.dump(model, model_path)
    print(f"✅ Model saved       → {model_path}")

    joblib.dump(list(X_train.columns), "models/feature_columns.pkl")
    print("✅ Feature columns   → models/feature_columns.pkl")

# ── Archive old reference, then promote new data as the baseline ───────────────
# Every old reference.csv is versioned into data/history/ before being overwritten.
# This means ANY previously used reference is always available for future drift checks.
import shutil

os.makedirs("data/history", exist_ok=True)

existing_snapshots = [f for f in os.listdir("data/history") if f.startswith("reference_v")]
snap_version       = len(existing_snapshots) + 1
snapshot_path      = f"data/history/reference_v{snap_version}.csv"

shutil.copy("data/reference.csv", snapshot_path)
print(f"\n📦 Old reference archived → {snapshot_path}")

# Now overwrite reference.csv with the data we just trained on
shutil.copy(args.new_data, "data/reference.csv")

print(f"🔄 data/reference.csv updated  ←  {args.new_data}")
print("✅ Retraining complete!\n")

# Print all available snapshots so the user knows what they can compare against
snapshots = sorted(os.listdir("data/history"))
print("📂 Available historical references for drift checks:")
for s in snapshots:
    print(f"   python drift.py --current data/history/{s}")
print("\n   python drift.py --current data/reference.csv  # → should show NO drift now")