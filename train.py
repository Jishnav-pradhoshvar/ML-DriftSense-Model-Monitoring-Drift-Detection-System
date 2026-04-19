import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn

os.makedirs("models", exist_ok=True)
mlflow.set_experiment("Churn Prediction")


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop(columns=["customerID"], errors="ignore")

    # Coerce any object column that looks numeric (e.g. TotalCharges in Telco dataset)
    for col in df.select_dtypes(include="object").columns:
        if col == "Churn":
            continue
        coerced = pd.to_numeric(df[col], errors="coerce")
        if coerced.notna().mean() > 0.8:   # >80% parsed successfully → treat as numeric
            df[col] = coerced

    df = df.dropna()

    # Robust Churn encoding — works whether values are "Yes/No", "1/0", True/False, etc.
    df["Churn"] = (df["Churn"].astype(str).str.strip().str.lower()
                   .isin(["yes", "1", "true"])).astype(int)

    df = pd.get_dummies(df)
    return df


df = preprocess(pd.read_csv("data/reference.csv"))

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
    print(f"Accuracy: {acc:.4f}")

    mlflow.log_param("n_estimators", N_ESTIMATORS)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

    existing  = [f for f in os.listdir("models") if f.startswith("model_v")]
    version   = len(existing) + 1
    model_path = f"models/model_v{version}.pkl"
    joblib.dump(model, model_path)
    print(f"✅ Model saved       → {model_path}")

    # Save feature columns so retrain can align columns later
    joblib.dump(list(X_train.columns), "models/feature_columns.pkl")
    print("✅ Feature columns   → models/feature_columns.pkl")