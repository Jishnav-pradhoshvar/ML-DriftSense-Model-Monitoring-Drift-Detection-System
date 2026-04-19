import argparse
import os
import subprocess
import sys
from pathlib import Path
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# ── Args ───────────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--reference",   default="data/reference.csv")
parser.add_argument("--current",     default="data/current.csv")
parser.add_argument("--drift-share", type=float, default=0.03,
                    help="Fraction of features that must drift to flag dataset drift (default 0.3)")
args = parser.parse_args()

os.makedirs("reports", exist_ok=True)
script_dir = Path(__file__).resolve().parent


# ── Preprocessing (same logic as train.py / retrain.py) ───────────────────────
def preprocess_for_drift(path: str) -> pd.DataFrame:
    """
    Light preprocessing for Evidently:
    - Drop ID column
    - Coerce pseudo-numeric object columns (e.g. TotalCharges)
    - Drop nulls
    Keep original categorical columns as strings so Evidently can run
    categorical drift tests on them automatically.
    """
    df = pd.read_csv(path)
    df = df.drop(columns=["customerID"], errors="ignore")

    for col in df.select_dtypes(include="object").columns:
        coerced = pd.to_numeric(df[col], errors="coerce")
        if coerced.notna().mean() > 0.8:
            df[col] = coerced

    df = df.dropna()
    return df


reference = preprocess_for_drift(args.reference)
current   = preprocess_for_drift(args.current)

# Align columns — Evidently requires both DataFrames to have identical schema
shared_cols = [c for c in reference.columns if c in current.columns]
reference   = reference[shared_cols]
current     = current[shared_cols]

print(f"📂 Reference : {args.reference}  ({len(reference)} rows, {len(shared_cols)} columns)")
print(f"📂 Current   : {args.current}  ({len(current)} rows)")

# ── Run Evidently ──────────────────────────────────────────────────────────────
report = Report(metrics=[DataDriftPreset(drift_share=args.drift_share)])
report.run(reference_data=reference, current_data=current)

report_path = "reports/drift_report.html"
report.save_html(report_path)
print(f"\n📊 Drift report saved → {report_path}")

# ── Parse results ──────────────────────────────────────────────────────────────
result          = report.as_dict()
metrics         = result["metrics"][0]["result"]
dataset_drifted = metrics["dataset_drift"]
n_drifted       = metrics["number_of_drifted_columns"]
n_total         = metrics["number_of_columns"]

# Show which specific columns drifted (fully dynamic — no column hardcoded)
print(f"\n{'Column':<30} {'Drift?':<10} {'p-value'}")
print("-" * 55)
for col_name, col_data in metrics.get("drift_by_columns", {}).items():
    drifted_flag = col_data.get("drift_detected", False)
    p_val        = col_data.get("drift_score", "N/A")
    marker       = "⚠️ YES" if drifted_flag else "✅ no"
    p_str        = f"{p_val:.4f}" if isinstance(p_val, float) else str(p_val)
    print(f"{col_name:<30} {marker:<10} {p_str}")

print(f"\n📈 Drifted columns : {n_drifted} / {n_total}")
print(f"🔍 Dataset drift   : {dataset_drifted}")

# ── Auto-retrain if drift detected ────────────────────────────────────────────
if dataset_drifted:
    print(f"\n⚠️  Drift detected → triggering retrain on {args.current} …\n")
    subprocess.run(
        [sys.executable, str(script_dir / "retrain.py"), "--new-data", args.current],
        check=True,
    )
else:
    print("\n✅ No significant drift — model is still valid, no retraining needed.")
