# 🧱 Project Architecture

## 📁 Folder Structure

```
customer-churn-ml-system/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── config/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── evaluation/
│   ├── api/
│   └── utils/
│
├── models/
├── config.yaml
├── requirements.txt
└── run.py
```

---

## 🧠 Layered Design

### 1. Config Layer

- Central configuration
- No hardcoding

### 2. Data Layer

- Load and clean data

### 3. Feature Layer

- Transform data for ML

### 4. Model Layer

- Train and predict

### 5. Evaluation Layer

- Measure performance

### 6. API Layer

- Serve predictions

### 7. Utils Layer

- Logging and helpers

---

## 🔁 Data Flow

### Training Flow

```
Raw Data → Preprocess → Features → Train → Save Model
```

### Prediction Flow

```
Input → API → Load Model → Predict → Response
```

---

## 🎯 Key Principles

- Separation of concerns
- Reusability
- Scalability
- Environment independence

---

## 🚀 Deployment Strategy

- Same code runs locally and on EC2
- Only environment changes (IP/port)
- Model stored on server

---

## ⚠️ Constraints

- No Docker
- No CI/CD
- Free-tier friendly
- Lightweight

---
