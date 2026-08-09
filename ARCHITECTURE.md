# 🧱 Project Architecture (Scalable Design)

---

## 📁 Folder Structure

```text
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
    │   │   └── config_loader.py
    │   │
    │   ├── data/
    │   │   └── preprocess.py
    │   │
    │   ├── features/
    │   │   └── feature_engineering.py
    │   │
    │   ├── models/
    │   │   ├── train_model.py
    │   │   ├── predict_model.py
    │   │   └── model_loader.py
    │   │
    │   ├── evaluation/
    │   │   └── evaluate.py
    │   │
    │   ├── services/
    │   │   └── prediction_service.py
    │   │
    │   ├── api/
    │   │   ├── main.py
    │   │   ├── routes/
    │   │   │   └── predict.py
    │   │   └── schemas/
    │   │       └── prediction_schema.py
    │   │
    │   └── utils/
    │       ├── logger.py
    │       └── helpers.py
    │
    ├── models/
    │
    ├── config.yaml
    ├── requirements.txt
    └── run.py
```

---

## 🧠 Layered Design

### 1. Config Layer

- Central configuration
- No hardcoding
- Used across all modules

---

### 2. Data Layer

- Data loading
- Data cleaning
- No ML logic

---

### 3. Feature Layer

- Feature transformation
- Encoding & scaling
- Shared between training & inference

---

### 4. Model Layer

- Model training
- Model loading
- Prediction logic
- No API or request handling

---

### 5. Evaluation Layer

- Metrics computation
- Cross-validation
- Model performance tracking

---

### 6. Service Layer

- Orchestrates prediction flow
- Combines preprocessing + model + logic
- Bridge between API and ML

---

### 7. API Layer

- FastAPI endpoints
- Request validation
- Response formatting
- No ML logic inside

---

### 8. Utils Layer

- Logging
- Helper functions
- Shared utilities

---

## 🔁 Data Flow

### 🔹 Training Flow

    Raw Data
       ↓
    Data Layer
       ↓
    Feature Layer
       ↓
    Model Layer (train)
       ↓
    Evaluation Layer
       ↓
    Save Model

---

### 🔹 Prediction Flow

    User Input
       ↓
    API Layer
       ↓
    Service Layer
       ↓
    Model Loader
       ↓
    Preprocessor
       ↓
    Model Prediction
       ↓
    Response

---

## 🎯 Key Principles

- Separation of concerns
- Reusability
- Scalability
- No ML logic in API
- No business logic in API
- Config-driven system

---

## 🚀 Deployment Strategy

- Same code runs locally and on EC2
- Only config/environment changes
- Model stored in `/models`
- API served via public IP

---

## ⚠️ Constraints

- No Docker
- No CI/CD
- Free-tier AWS only
- Lightweight setup

---

## 🔮 Future Scalability

- Multiple model support
- Model versioning
- Background jobs
- Caching (Redis)
- Monitoring & logging

---
