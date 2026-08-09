# 🚀 Customer Churn ML System

## 📌 Overview

This project is a **production-ready Machine Learning system** that predicts customer churn.

It includes:

- End-to-end ML pipeline (data → model)
- FastAPI-based prediction service
- Deployment on AWS EC2 (Free Tier)
- Config-driven architecture (no hardcoding)

---

## 🎯 Objective

Build a system that:

- Trains a churn prediction model locally
- Serves predictions via API
- Runs identically on local and cloud environments

---

## 🧠 Architecture Philosophy

- Layered architecture
- Separation of concerns
- Train once → serve everywhere
- No environment-specific code

---

## ⚙️ Tech Stack

### ML

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost

### API

- FastAPI
- Uvicorn
- Pydantic

### Deployment

- AWS EC2 (Free Tier)

---

## 🔁 System Flow

```
Training:
Data → Preprocessing → Features → Model → Save (.pkl)

Inference:
Input → API → Load Model → Predict → Output
```

---

## 📦 Output

```
{
  "prediction": 0 or 1,
  "probability": 0.87
}
```

---

## 🚀 How to Run (Local)

```
uvicorn src.api.main:app --reload
```

Visit:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Deployment

- Deploy on AWS EC2
- Run with:

```
uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

---

## ⚠️ Important Rules

- No hardcoded paths
- No training inside API
- Config-driven system
- Same code for local & cloud

---

## 🧠 Key Learning Outcomes

- ML system design
- API integration
- Cloud deployment
- Production thinking

---
