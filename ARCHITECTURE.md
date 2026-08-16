# 🧱 Customer Churn ML System — Project Architecture

---

## 📌 Architecture Overview

This project is designed as a modular, layered **Machine Learning Engineering system** rather than a simple ML notebook.

The complete system follows:

```text
Data
  ↓
Preprocessing
  ↓
Model Training
  ↓
Model Artifact
  ↓
FastAPI
  ↓
Prediction Service
  ↓
Database Repository
  ↓
PostgreSQL
  ↓
Docker / Docker Compose
  ↓
CI/CD
  ↓
AWS EC2
  ↓
Nginx
  ↓
Public API
  ↓
CloudWatch
  ↓
S3 Model Backup
```

The project is intentionally lightweight and focuses on understanding the complete ML engineering lifecycle without introducing unnecessary production complexity.

---

# 📁 Final Repository Structure

```text
customer-churn-ml-system/
│
├── .dockerignore
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── ARCHITECTURE.md
├── README.md
├── ROADMAP.md
│
├── config.yaml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
│
├── Dockerfile
├── docker-compose.yml
│
├── run.py
├── train.py
│
├── data/
│   ├── churn.db
│   └── raw/
│       └── churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── main.py
│   │   │
│   │   ├── routes/
│   │   │   └── prediction.py
│   │   │
│   │   └── schemas/
│   │       └── prediction_schema.py
│   │
│   ├── config/
│   │   └── config_loader.py
│   │
│   ├── data/
│   │   └── preprocess.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── model_loader.py
│   │   ├── predict_model.py
│   │   ├── prediction.py
│   │   └── train_model.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── prediction_repository.py
│   │
│   ├── services/
│   │   └── prediction_service.py
│   │
│   └── utils/
│       └── logger.py
│
└── tests/
    ├── conftest.py
    ├── test_health.py
    ├── test_prediction.py
    └── test_startup.py
```

> Runtime-generated directories such as `.git/`, `__pycache__/`, `.pytest_cache/`, and compiled `.pyc` files are intentionally omitted from the architecture because they are not part of the application's logical architecture.

---

# 🧠 Layered Architecture

The application follows a separation-of-concerns approach.

```text
┌───────────────────────────────────────────────┐
│                   API Layer                    │
│          FastAPI + Request Validation          │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│                Service Layer                   │
│          Prediction orchestration              │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│                 Model Layer                    │
│       Model loading + prediction logic         │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│                Data / Model                    │
│       Preprocessing + ML Pipeline              │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│             Repository Layer                   │
│          Prediction persistence                │
└───────────────────────┬───────────────────────┘
                        ↓
┌───────────────────────────────────────────────┐
│               Database Layer                   │
│          SQLAlchemy + PostgreSQL               │
└───────────────────────────────────────────────┘
```

---

# 1. ⚙️ Configuration Layer

Location:

```text
src/config/
└── config_loader.py
```

### Responsibilities

- Load centralized configuration.
- Keep configuration separate from application logic.
- Provide configuration values to different components.
- Reduce hardcoded configuration values.

Main configuration file:

```text
config.yaml
```

The same configuration approach is used across local development and deployment environments.

---

# 2. 📊 Data Layer

Location:

```text
src/data/
└── preprocess.py
```

### Responsibilities

- Load and prepare customer churn data.
- Perform data cleaning.
- Convert required data types.
- Handle missing values.
- Prepare data for the ML pipeline.

Raw dataset:

```text
data/raw/churn.csv
```

The data layer does not contain API or HTTP logic.

---

# 3. 🤖 Model Layer

Location:

```text
src/models/
├── model_loader.py
├── predict_model.py
├── prediction.py
└── train_model.py
```

The model layer contains the core ML functionality.

### `train_model.py`

Responsible for model training.

The project uses:

```text
XGBoost Classifier
```

Training is separated from API serving.

### `model_loader.py`

Responsible for loading the saved model artifact used by the application.

### `predict_model.py`

Contains prediction-related model operations.

### `prediction.py`

Contains model prediction-related structures/logic used by the application.

### Model Artifact

The trained model is stored at:

```text
models/churn_model.pkl
```

The artifact contains the trained preprocessing/model pipeline and prediction threshold required for inference.

---

# 4. 🗄️ Database Layer

Location:

```text
src/database/
├── __init__.py
└── database.py
```

### Responsibilities

- Configure database connectivity.
- Create/manage database sessions.
- Provide database infrastructure to the application.

The application uses SQLAlchemy for database interaction.

During deployment, PostgreSQL runs as a Docker Compose service.

---

# 5. 📚 Repository Layer

Location:

```text
src/repositories/
├── __init__.py
└── prediction_repository.py
```

The repository layer separates database persistence logic from business/application logic.

### Responsibilities

- Store prediction records.
- Retrieve prediction records.
- Interact with the database layer.
- Keep database queries outside API routes.

This creates a clean separation:

```text
Service
   ↓
Repository
   ↓
Database
```

---

# 6. 🔧 Service Layer

Location:

```text
src/services/
└── prediction_service.py
```

The service layer orchestrates the prediction workflow.

### Responsibilities

- Receive validated prediction input.
- Coordinate model loading/prediction.
- Apply prediction-related logic.
- Determine risk level.
- Coordinate prediction persistence.
- Return application-level results to the API layer.

The service layer acts as the bridge between:

```text
API
 ↓
ML System
 ↓
Database
```

The API routes remain intentionally thin.

---

# 7. 🚀 API Layer

Location:

```text
src/api/
├── main.py
├── routes/
│   └── prediction.py
└── schemas/
    └── prediction_schema.py
```

The API layer exposes the ML system through FastAPI.

## `main.py`

Responsible for:

- FastAPI application creation.
- Application startup.
- API registration.
- Application-level configuration.

---

## API Routes

### `POST /predict`

Performs customer churn prediction.

Flow:

```text
Customer Input
      ↓
Pydantic Validation
      ↓
Prediction Service
      ↓
Model
      ↓
Probability
      ↓
Threshold
      ↓
Risk Level
      ↓
Database
      ↓
Response
```

---

### `GET /health`

Used to verify that the API service is alive and available.

```text
Client
  ↓
/health
  ↓
FastAPI
  ↓
Health Response
```

This endpoint is also useful for deployment verification and monitoring.

---

### `POST /explain`

Provides an explainability response for a churn prediction.

The endpoint uses SHAP-based explanation to expose feature-level contribution information.

Conceptual flow:

```text
Customer Input
      ↓
Prediction
      ↓
SHAP Explanation
      ↓
Feature Contributions
      ↓
Explanation Response
```

---

# 8. 🧾 Schema Layer

Location:

```text
src/api/schemas/
└── prediction_schema.py
```

### Responsibilities

- Define API request structures.
- Validate incoming customer data.
- Define API response structures.
- Restrict categorical values.
- Validate numerical ranges.

This keeps request validation separate from prediction/business logic.

---

# 9. 📝 Logging / Utility Layer

Location:

```text
src/utils/
└── logger.py
```

### Responsibilities

- Application logging.
- Centralized logging configuration.
- Supporting debugging and runtime observability.

Logs can be viewed locally through Docker/container logs and were also integrated with CloudWatch during AWS deployment.

---

# 10. 🧪 Testing Layer

Location:

```text
tests/
├── conftest.py
├── test_health.py
├── test_prediction.py
└── test_startup.py
```

Testing uses:

```text
pytest
```

### Test coverage includes

- Application startup.
- Health endpoint.
- Prediction endpoint.
- Valid prediction requests.
- Invalid requests.
- Validation failures.
- Prediction behavior.

The testing configuration is defined through:

```text
pytest.ini
```

Development/testing dependencies are separated into:

```text
requirements-dev.txt
```

---

# 🔄 Machine Learning Training Flow

The training process is separated from API serving.

Entry point:

```text
train.py
```

Conceptual flow:

```text
Raw Dataset
     ↓
Data Preprocessing
     ↓
Feature Processing
     ↓
Train/Test Split
     ↓
Preprocessing Pipeline
     ↓
XGBoost Classifier
     ↓
Model Evaluation
     ↓
Threshold Selection
     ↓
Saved Model Artifact
```

Output:

```text
models/churn_model.pkl
```

---

# 🔮 Prediction Flow

The complete inference flow is:

```text
Client
   ↓
FastAPI
   ↓
Pydantic Validation
   ↓
Prediction Route
   ↓
Prediction Service
   ↓
Model Loader
   ↓
Preprocessing Pipeline
   ↓
XGBoost Model
   ↓
Churn Probability
   ↓
Prediction Threshold
   ↓
Risk Level
   ↓
Prediction Repository
   ↓
PostgreSQL
   ↓
API Response
```

---

# 💡 Explainability Flow

For `/explain`:

```text
Client
   ↓
FastAPI
   ↓
Validation
   ↓
Prediction Service
   ↓
Model Prediction
   ↓
SHAP
   ↓
Feature Contributions
   ↓
Risk / Prediction Information
   ↓
API Response
```

Explanation requests are not part of the prediction-history persistence flow.

---

# 🗃️ Database Persistence Flow

Prediction requests have a persistence component:

```text
POST /predict
      ↓
Prediction Service
      ↓
Prediction Repository
      ↓
SQLAlchemy
      ↓
PostgreSQL
```

The stored information includes prediction-related information such as:

```text
Prediction
Probability
Risk Level
Timestamp
```

This allows the project to demonstrate how an ML API can persist prediction history.

---

# 🐳 Docker Architecture

The application is containerized using Docker.

Main files:

```text
Dockerfile
docker-compose.yml
.dockerignore
```

The Docker image contains the FastAPI application and its ML dependencies.

The application container exposes:

```text
8000
```

---

# 🐳 Docker Compose Architecture

Docker Compose is used to run the application stack.

Conceptually:

```text
Docker Compose
      │
      ├── FastAPI / ML API
      │
      └── PostgreSQL
```

The API communicates with PostgreSQL through the Docker Compose network.

The database data is persisted through the configured Docker volume.

---

# 🔁 Docker Compose Request Flow

```text
Internet / Client
       ↓
FastAPI Container
       ↓
Prediction Service
       ↓
ML Model
       ↓
PostgreSQL Container
```

This allows the entire application stack to be started together.

Example:

```bash
docker compose up --build
```

---

# 🔄 CI/CD Architecture

GitHub Actions is used for continuous integration.

Workflow:

```text
Git Push / Pull Request
          ↓
    GitHub Actions
          ↓
 Install Dependencies
          ↓
      Run Tests
          ↓
 Build Docker Image
          ↓
      CI Result
```

Workflow file:

```text
.github/
└── workflows/
    └── ci.yml
```

The CI pipeline verifies that changes can be tested and the Docker image can be built successfully.

---

# ☁️ AWS Deployment Architecture

The application was temporarily deployed to AWS for learning, verification, and demonstration.

High-level architecture:

```text
Internet
   ↓
Public IPv4
   ↓
Nginx
   ↓
FastAPI
   ↓
Docker
   ↓
ML Model
   ↓
PostgreSQL
```

The EC2 instance hosted the Dockerized application stack.

---

# 🖥️ AWS EC2

The application was deployed on an Amazon EC2 instance.

EC2 responsibilities:

- Host the application.
- Run Docker.
- Run Docker Compose.
- Host the ML model.
- Serve the FastAPI application.
- Run PostgreSQL through Docker Compose.
- Provide public access during demonstration.

The EC2 instance was intentionally kept lightweight because this is a learning and portfolio project.

After demonstration, the instance was stopped for cost safety.

---

# 🌐 Nginx

Nginx was used as a reverse proxy between the public internet and the FastAPI application.

Architecture:

```text
Client
  ↓
Public IP
  ↓
Nginx
  ↓
FastAPI
  ↓
Application
```

This demonstrates the role of a reverse proxy in front of an application server.

---

# 📦 S3 Model Backup

Amazon S3 was used for model artifact backup.

Architecture:

```text
Trained Model
      ↓
churn_model.pkl
      ↓
S3 Bucket
```

The purpose of S3 in this project is intentionally limited to:

```text
Model Artifact Backup / Storage
```

The application does not depend on S3 for every prediction request.

The local/deployed application continues to use the model artifact available to it.

---

# 📊 CloudWatch

Amazon CloudWatch was used for basic cloud monitoring and application logging.

Conceptual flow:

```text
Application
    ↓
Application Logs
    ↓
CloudWatch
    ↓
Log Group
    ↓
Log Stream
```

CloudWatch allowed deployed API activity and application events to be inspected during the demonstration.

The project intentionally avoids expensive or unnecessarily complex monitoring infrastructure.

---

# 🔐 AWS Cost-Safety Design

The deployment was designed around temporary learning usage rather than 24/7 production hosting.

The project intentionally avoided:

```text
❌ NAT Gateway
❌ Load Balancer
❌ RDS
❌ Elastic IP
❌ GPU
❌ Kubernetes
❌ Complex monitoring infrastructure
```

The deployed EC2 instance was stopped after the demonstration.

The model backup in S3 and required storage resources were retained so the project remains recoverable.

---

# 📈 Complete Deployment Flow

```text
                         ┌─────────────────────┐
                         │       Client        │
                         └──────────┬──────────┘
                                    │
                                    ↓
                         ┌─────────────────────┐
                         │    Public Internet  │
                         └──────────┬──────────┘
                                    │
                                    ↓
                         ┌─────────────────────┐
                         │       Nginx         │
                         │   Reverse Proxy     │
                         └──────────┬──────────┘
                                    │
                                    ↓
                         ┌─────────────────────┐
                         │     FastAPI API     │
                         │ /health             │
                         │ /predict            │
                         │ /explain            │
                         └──────────┬──────────┘
                                    │
                                    ↓
                         ┌─────────────────────┐
                         │ Prediction Service  │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ↓                               ↓
          ┌──────────────────┐             ┌──────────────────┐
          │   ML Pipeline    │             │    Repository    │
          │                  │             │      Layer       │
          │ Preprocessing    │             └────────┬─────────┘
          │       ↓          │                      │
          │    XGBoost       │                      ↓
          │       ↓          │             ┌──────────────────┐
          │ Prediction       │             │   PostgreSQL     │
          └──────────────────┘             └──────────────────┘
                    │
                    ↓
          ┌────────────────────┐
          │ churn_model.pkl    │
          └────────────────────┘


        Supporting Infrastructure
        ──────────────────────────

        GitHub
           ↓
        GitHub Actions
           ↓
        Tests + Docker Build


        Model Backup
        ────────────
        churn_model.pkl
              ↓
             S3


        Monitoring
        ──────────
        Application / EC2 Logs
              ↓
          CloudWatch
```

---

# 🎯 Key Architectural Principles

### 1. Separation of Concerns

Each layer has a defined responsibility.

```text
API
 ↓
Service
 ↓
Model / Repository
 ↓
Infrastructure
```

---

### 2. Thin API Layer

API routes are responsible primarily for:

- Receiving requests.
- Validation.
- Calling services.
- Returning responses.

ML and persistence logic are not intentionally placed directly inside the routes.

---

### 3. Reusable ML Pipeline

The preprocessing and model pipeline is packaged together so the same transformations can be applied consistently during inference.

```text
Input
 ↓
Preprocessing
 ↓
Model
 ↓
Prediction
```

---

### 4. Database Separation

Database access is separated into:

```text
Database Layer
      ↓
Repository Layer
      ↓
Service Layer
```

This prevents database-specific logic from spreading throughout the application.

---

### 5. Configuration-Driven Design

Configuration is centralized through:

```text
config.yaml
```

This reduces hardcoded configuration and makes the application easier to adapt between environments.

---

### 6. Containerized Deployment

The application can be run consistently through:

```text
Docker
Docker Compose
```

This reduces environment differences between development and deployment.

---

### 7. Automated Verification

GitHub Actions automatically verifies:

```text
Dependencies
    ↓
Tests
    ↓
Docker Build
```

---

# 🚀 Local vs Cloud Architecture

## Local Development

```text
Developer
   ↓
FastAPI
   ↓
Docker Compose
   ├── API
   └── PostgreSQL
```

---

## AWS Deployment

```text
Internet
   ↓
EC2
   ↓
Nginx
   ↓
Docker Compose
   ├── FastAPI
   └── PostgreSQL

Additional AWS Services:
   ├── S3 → Model Backup
   └── CloudWatch → Logging / Monitoring
```

The application architecture remains largely the same between environments; the main difference is the infrastructure surrounding the application.

---

# 🛠️ Main Entry Points

## Training

```bash
python train.py
```

Purpose:

```text
Dataset
  ↓
Training
  ↓
Evaluation
  ↓
Model Artifact
```

---

## Local Application

```bash
python run.py
```

The application can also be run through Docker Compose:

```bash
docker compose up --build
```

---

## Testing

```bash
pytest
```

---

# 📦 Important Project Artifacts

| Artifact                   | Purpose                           |
| -------------------------- | --------------------------------- |
| `train.py`                 | Training entry point              |
| `run.py`                   | Application entry point           |
| `config.yaml`              | Central configuration             |
| `models/churn_model.pkl`   | Trained ML artifact               |
| `Dockerfile`               | Application container definition  |
| `docker-compose.yml`       | Multi-container application stack |
| `.github/workflows/ci.yml` | CI pipeline                       |
| `pytest.ini`               | Pytest configuration              |
| `requirements.txt`         | Runtime dependencies              |
| `requirements-dev.txt`     | Development/testing dependencies  |
| `README.md`                | Complete project documentation    |
| `ROADMAP.md`               | Project development roadmap       |
| `ARCHITECTURE.md`          | System architecture               |

---

# 🏁 Final Architecture Summary

This project demonstrates a complete ML engineering workflow:

```text
                 MACHINE LEARNING
                       │
                       ↓
              ┌─────────────────┐
              │ Data Processing │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ XGBoost Model   │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Model Artifact  │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │    FastAPI      │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Prediction      │
              │ Service         │
              └───────┬─────────┘
                      / \
                     /   \
                    ↓     ↓
             ┌─────────┐ ┌────────────┐
             │   ML    │ │ Repository │
             └─────────┘ └──────┬─────┘
                                ↓
                         ┌─────────────┐
                         │ PostgreSQL  │
                         └─────────────┘

             ───── Deployment ─────

                  Docker Compose
                       ↓
                      EC2
                       ↓
                     Nginx
                       ↓
                  Public API

             ───── Supporting AWS ─────

                  S3 → Model Backup
                  CloudWatch → Logs

             ───── Engineering ─────

              GitHub → GitHub Actions
                       ↓
                 Tests + Build
```

The architecture intentionally balances **real ML engineering practices** with a manageable learning scope.

It demonstrates:

- Machine learning
- Reproducible preprocessing
- Model packaging
- FastAPI
- API validation
- Explainable AI with SHAP
- SQLAlchemy
- PostgreSQL
- Repository pattern
- Automated testing
- Docker
- Docker Compose
- GitHub Actions
- AWS EC2
- Nginx
- S3
- CloudWatch
- Public API deployment

without introducing unnecessary complexity such as Kubernetes, microservices, RDS, load balancers, NAT gateways, Redis, Kafka, or other infrastructure that is outside the learning objective of this project.
