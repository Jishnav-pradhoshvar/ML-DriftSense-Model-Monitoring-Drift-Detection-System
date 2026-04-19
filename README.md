<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=ML%20DriftSense&fontSize=72&fontColor=ffffff&fontAlignY=38&desc=ML%20Model%20Monitoring%20%26%20Drift%20Detection%20System&descAlignY=60&descSize=20&animation=fadeIn" width="100%"/>

<!-- Animated Typing SVG -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&duration=3000&pause=800&color=A78BFA&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=80&lines=🔍+Detect+Drift+Before+It+Hurts+Your+Model;🤖+Auto-Retrain+When+Performance+Drops;📊+Real-Time+Monitoring+Dashboard" alt="Typing SVG" />
</a>

<br/>

<!-- Badges Row 1 -->
<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

<br/>

<!-- Badges Row 2 -->
<img src="https://img.shields.io/badge/Evidently%20AI-8B5CF6?style=for-the-badge&logo=ai&logoColor=white"/>
<img src="https://img.shields.io/badge/Status-Production%20Ready-22c55e?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Level-Intermediate-ec4899?style=for-the-badge"/>

<br/><br/>

</div>

---

## 🌊 What is ML DriftSense?

> **ML DriftSense** is a production-ready system that **continuously watches your ML model**, catches when the world has changed around it, and **heals itself automatically** — so your predictions stay accurate, always.

In the real world, data distributions shift. User behavior evolves. ML models go stale. Most teams don't notice until something breaks. **DriftSense makes sure you're not one of them.**

---

## 🧩 The Problem It Solves

```
    Real World Changes          →   Your Model Doesn't Know
    ───────────────────             ─────────────────────────
    User behavior shifts        →   Still predicts like it's last year
    Data distributions change   →   Silent, undetected degradation
    Business conditions evolve  →   Wrong decisions. Every day.
```

Without monitoring, degraded models silently destroy trust and revenue. **DriftSense gives your model self-awareness.**

---

## ⚡ Key Features

<table>
<tr>
<td width="50%">

### 🔬 Statistical Drift Detection
Uses **Evidently AI** to compare reference vs. current data distributions using industry-grade statistical tests. Not just value changes — actual distribution shifts.

</td>
<td width="50%">

### 🔁 Auto-Retraining Pipeline
When drift exceeds your threshold, the system **automatically triggers retraining** on new data — no manual intervention required.

</td>
</tr>
<tr>
<td width="50%">

### 📈 Experiment Tracking with MLflow
Every training run is logged — accuracy, parameters, model versions. Full lineage of what changed and when.

</td>
<td width="50%">

### 🖥️ Live Streamlit Dashboard
A real-time visual interface showing model health, drift reports, and monitoring insights — all in one place.

</td>
</tr>
</table>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        ML DRIFTSENSE                            │
│                                                                 │
│   📂 Training Data                                              │
│         │                                                       │
│         ▼                                                       │
│   🤖 Model Training (RandomForest)  ──────► 📊 MLflow Tracking │
│         │                                                       │
│         ▼                                                       │
│   📥 New Incoming Data                                          │
│         │                                                       │
│         ▼                                                       │
│   🔍 Drift Detection (Evidently AI)                             │
│         │                                                       │
│    ┌────┴─────────────────────┐                                 │
│    │ Drift Detected?          │                                 │
│    │                          │                                 │
│   YES                         NO                                │
│    │                          │                                 │
│    ▼                          ▼                                 │
│ 🔄 Auto Retrain          ✅ Continue Monitoring                 │
│    │                                                            │
│    ▼                                                            │
│ 💾 New Model Saved + Logged to MLflow                           │
│    │                                                            │
│    ▼                                                            │
│ 📺 Streamlit Dashboard Updates                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Tool | Role | Why It Was Chosen |
|------|------|-------------------|
| ![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square) | Model Training | Battle-tested RandomForest classifier |
| ![MLflow](https://img.shields.io/badge/-MLflow-0194E2?logo=mlflow&logoColor=white&style=flat-square) | Experiment Tracking | Full lifecycle management, versioning |
| ![Evidently](https://img.shields.io/badge/-Evidently%20AI-8B5CF6?style=flat-square) | Drift Detection | Industry-standard statistical tests |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square) | Dashboard UI | Rapid, beautiful ML dashboards |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square) | Data Processing | Flexible tabular data handling |
| ![Joblib](https://img.shields.io/badge/-Joblib-grey?style=flat-square) | Model Serialization | Fast, reliable model save/load |

---

## 📁 Project Structure

```
ml_driftSense/
│
├── 📂 data/
│   ├── reference.csv          # Baseline training data
│   └── current.csv            # Incoming production data
│
├── 📂 models/
│   └── model.pkl              # Trained model artifact
│
├── 📂 reports/
│   └── drift_report.html      # Evidently drift report
│
├── 📂 src/
│   ├── train.py               # Initial model training
│   ├── drift.py               # Drift detection logic
│   ├── retrain.py             # Auto-retraining script
│   └── modify_data.py         # Drift simulation utility
│
├── 📂 app/
│   └── dashboard.py           # Streamlit monitoring UI
│
├── 📂 mlruns/                 # MLflow experiment logs
└── requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ml-driftsense.git
cd ml-driftsense
```

### 2️⃣ Create & Activate Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas numpy scikit-learn matplotlib streamlit mlflow evidently joblib
```

---

## ▶️ Running the Project (End-to-End)

```bash
# Step 1: Train the initial model
python src/train.py

# Step 2: Simulate real-world data drift
python src/modify_data.py

# Step 3: Run drift detection (triggers auto-retrain if drift found)
python src/drift.py

# Step 4: Launch the monitoring dashboard
streamlit run app/dashboard.py

# Step 5: View experiment history in MLflow
mlflow ui
# Open: http://127.0.0.1:5000
```

---

## 🔍 How Drift Detection Works

Drift detection uses **statistical distribution comparison**, not just value changes.

```python
# The drift threshold configuration
drift_share = 0.1   # 10% of columns must show drift to trigger alert
                    # Lower this (e.g., 0.03) to catch subtler drift
```

| Scenario | Result |
|----------|--------|
| A few row values changed | ❌ No drift detected (distribution unchanged) |
| All values set to a constant | ❌ No drift (no variance for statistical test) |
| Distribution genuinely shifts | ✅ Drift detected → Auto-retrain triggered |

> 💡 **Key Insight:** Drift is about *how data is distributed*, not individual values.

---

## 🧠 Core Concepts

<details>
<summary><strong>📌 What is Data Drift?</strong></summary>

Data drift occurs when the statistical properties of the model's input data change over time. For example, if your model was trained on user ages 18-35, but production data starts including ages 50-70, the model's predictions become unreliable.

</details>

<details>
<summary><strong>📌 What is Concept Drift?</strong></summary>

Concept drift is when the relationship between input features and the target label changes. For example, features that once predicted churn may no longer be reliable indicators because user behavior patterns have fundamentally shifted.

</details>

<details>
<summary><strong>📌 How does auto-retraining work?</strong></summary>

When `drift.py` detects drift above the configured threshold, it executes:

```python
if drifted:
    os.system("python src/retrain.py")
```

`retrain.py` trains a fresh model on the current (new) data, logs it to MLflow, and saves it — replacing the outdated model automatically.

</details>

---

## 📊 Dashboard Preview

The Streamlit dashboard shows:

- ✅ **Model Status** — Is a trained model available?
- 📉 **Drift Report** — Full HTML report from Evidently AI
- 🔢 **Monitoring Metrics** — Accuracy and performance over time
- 🔄 **Retraining History** — Via MLflow experiment logs

---

## 🐛 Known Issues & Solutions

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| `FileNotFoundError: data/current.csv` | Wrong working directory | Run scripts from project root |
| Drift not detected after small changes | Distribution unchanged | Shift entire column distributions, not individual rows |
| Constant values → no drift | No variance = stats test fails | Use random distributions instead of fixed values |
| Drift threshold too high | `drift_share=0.1` by default | Lower to `drift_share=0.03` for sensitive detection |

---

## 🔮 Roadmap

- [ ] Real-time data pipeline integration
- [ ] Email / Slack alert system when drift is detected
- [ ] Cloud deployment (AWS SageMaker / GCP Vertex AI)
- [ ] Prediction monitoring (output drift)
- [ ] Multi-model support
- [ ] REST API for drift status checks

---

## 💬 Interview-Ready Explanation

> *"I built an end-to-end ML monitoring system that tracks model performance using MLflow, detects data drift using Evidently AI, and automatically retrains the model when drift exceeds a defined threshold. The system includes a Streamlit dashboard for real-time monitoring and ensures continuous model reliability in production."*

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

<div align="center">

<!-- Animated Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer&animation=fadeIn" width="100%"/>

**Built with 🧠 and ☕ | ML DriftSense — Because models shouldn't go blind in production.**

⭐ **Star this repo if you find it useful!**

</div>
