import streamlit as st
import os

st.set_page_config(page_title="ML Monitoring Dashboard", layout="wide")

st.title("📊 Model Monitoring & Drift Detection")

# Section 1 — Model Info
st.header("Model Info")

if os.path.exists("models/model.pkl"):
    st.success("Model is available")
else:
    st.error("Model not found")

# Section 2 — Drift Report
st.header("Drift Report")

report_path = "reports/drift_report.html"

if os.path.exists(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        html_data = f.read()
    st.components.v1.html(html_data, height=600, scrolling=True)
else:
    st.warning("Drift report not found. Run drift.py first.")