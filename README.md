# 🚀 Customer Churn ML System

> ### From raw customer data to a deployed, monitored Machine Learning API.

This repository contains a complete **end-to-end Machine Learning Engineering system** built around customer churn prediction.

The project deliberately goes beyond training a model in a notebook. It takes the model through the full journey:

**📊 Data → 🧹 Preprocessing → 🤖 Model Training → 📈 Evaluation → 📦 Model Packaging → ⚡ FastAPI → 🗄️ PostgreSQL → 🧪 Testing → 🐳 Docker → 🔗 Docker Compose → 🔄 CI/CD → ☁️ AWS EC2 → 🌐 Nginx → 🪣 S3 → 📡 CloudWatch → 🌍 Public API**

---

## 🎯 What This Project Is About

The central question is simple:

> **Can we take a machine learning model, turn it into an actual application, deploy it to the cloud, monitor it, verify it from the outside world, and safely shut the infrastructure down afterwards?**

**Yes.**

This project was built specifically to learn and demonstrate that complete lifecycle.

It is intentionally **not** a commercially productionized platform. The goal is to understand the engineering surrounding an ML model without introducing infrastructure that the project does not actually need.

### 🧭 The journey

| Stage                | What happens                                            |
| -------------------- | ------------------------------------------------------- |
| 📊 **Data**          | Explore and understand Telco Customer Churn data        |
| 🧹 **Pipeline**      | Clean, transform, encode, scale, and prepare features   |
| 🤖 **ML**            | Train an XGBoost churn classifier                       |
| 📈 **Evaluation**    | Measure performance and optimize for recall             |
| 📦 **Packaging**     | Save preprocessing + model + threshold together         |
| ⚡ **API**           | Expose predictions through FastAPI                      |
| 🗄️ **Persistence**   | Store prediction history in PostgreSQL                  |
| 🧪 **Testing**       | Automatically verify application behavior               |
| 🐳 **Containers**    | Package the application with Docker                     |
| 🔗 **Orchestration** | Run API + database with Docker Compose                  |
| 🔄 **CI**            | Automatically test and build through GitHub Actions     |
| ☁️ **Cloud**         | Deploy the system temporarily on AWS EC2                |
| 🌐 **Reverse Proxy** | Put Nginx in front of FastAPI                           |
| 🪣 **Backup**        | Store the trained model in S3                           |
| 📡 **Monitoring**    | Send application logs to CloudWatch                     |
| 🌍 **Verification**  | Test the complete system through the public API         |
| 🧹 **Cleanup**       | Shut down unnecessary AWS resources after demonstration |

> 💡 **The important part is not any single technology. The important part is seeing how all of these pieces connect around one ML model.**

---

## 🏆 Project Highlights

### 🤖 Machine Learning

- XGBoost binary classification
- End-to-end scikit-learn preprocessing pipeline
- Class weighting
- Custom decision threshold
- Recall-focused evaluation
- SHAP-based explainability

### ⚙️ Backend Engineering

- FastAPI
- Pydantic validation
- Modular prediction services
- PostgreSQL
- SQLAlchemy
- Prediction history

### 🐳 DevOps / CI

- Docker
- Docker Compose
- GitHub Actions
- Automated testing
- Container build verification

### ☁️ AWS

- EC2
- IAM role
- Security Group
- Nginx
- S3 model backup
- S3 restore verification
- CloudWatch logging

### 🌍 Deployment

- Public `/health`
- Public `/predict`
- Public `/explain`
- Public validation/error testing
- Database verification
- Centralized application logs

---

## 📊 Final Model Performance

| Metric       |     Result |
| ------------ | ---------: |
| 🎯 Accuracy  | **0.6802** |
| 🎯 Precision | **0.4477** |
| 🚨 Recall    | **0.8690** |
| 🎯 F1 Score  | **0.5909** |
| 📈 ROC-AUC   | **0.8247** |

> 🔎 **Why is precision relatively low?**  
> Because this project intentionally prioritizes **recall**. For churn detection, missing a customer who is actually going to leave can be more costly than flagging some customers who ultimately stay.

---

## 🧠 Core Engineering Idea

The model is not treated as an isolated `.pkl` file.

The actual system is:

**Raw Input → Validation → Preprocessing → XGBoost → Probability → Threshold → Prediction → Database → API Response**

And for explainability:

**Raw Input → Validation → Model → SHAP → Feature Contributions → Explanation**

The deployment then wraps that application with:

**Docker → Compose → CI → EC2 → Nginx → S3 → CloudWatch**

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Project Goals](#-project-goals)
- [System Architecture](#-system-architecture)
- [Dataset](#-dataset)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Feature Engineering](#-feature-engineering)
- [Model](#-model)
- [Decision Threshold](#-decision-threshold)
- [Model Evaluation](#-model-evaluation)
- [Model Packaging](#-model-packaging)
- [FastAPI Application](#-fastapi-application)
- [API Endpoints](#-api-endpoints)
- [API Validation](#-api-validation)
- [SHAP Explainability](#-shap-explainability)
- [Database](#-database)
- [SQLAlchemy](#-sqlalchemy)
- [Testing](#-testing)
- [Docker](#-docker)
- [Docker Compose](#-docker-compose)
- [CI/CD](#-cicd)
- [AWS Deployment](#-aws-deployment)
- [EC2](#-ec2)
- [IAM](#-iam)
- [Nginx](#-nginx)
- [S3 Model Backup](#-s3-model-backup)
- [S3 Restore Verification](#-s3-restore-verification)
- [CloudWatch](#-cloudwatch)
- [Public Deployment Flow](#-public-deployment-flow)
- [Public API Verification](#-public-api-verification)
- [Project Structure](#-project-structure)
- [Local Setup](#-local-setup)
- [Training the Model](#-training-the-model)
- [Running the Application](#-running-the-application)
- [Running with Docker Compose](#-running-with-docker-compose)
- [Running Tests](#-running-tests)
- [Example Prediction](#-example-prediction)
- [Example Explanation](#-example-explanation)
- [Key Engineering Decisions](#-key-engineering-decisions)
- [AWS Cost and Security Considerations](#-aws-cost-and-security-considerations)
- [What I Learned](#-what-i-learned)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Project Outcome](#-project-outcome)
- [Final Architecture](#-final-architecture)

---

# 📌 Project Overview

[⬆️ Back to Table of Contents](#-table-of-contents)
Customer churn prediction is a binary classification problem where the objective is to identify customers who are likely to leave a service.

The machine learning portion of this project uses the **Telco Customer Churn** dataset to train a model capable of predicting churn.

However, the main focus of this project is not only the model.

The larger objective was to build an end-to-end ML engineering system around the model.

The final system includes:

- Data preprocessing
- Feature processing
- XGBoost classification
- Model evaluation
- Model serialization
- Prediction thresholding
- FastAPI
- Pydantic validation
- SHAP explainability
- PostgreSQL
- SQLAlchemy
- Automated testing
- Docker
- Docker Compose
- GitHub Actions
- AWS EC2
- IAM
- Security Groups
- Nginx
- Amazon S3
- Amazon CloudWatch
- Public API testing

The final deployed API was tested from outside the EC2 instance through its public IP.

---

# 🎯 Problem Statement

[⬆️ Back to Table of Contents](#-table-of-contents)

> **Business perspective:** identify customers with a higher likelihood of churn so that retention efforts can focus on customers who need attention.

Customer churn can have a significant business impact because acquiring a new customer can be more expensive than retaining an existing one.

A churn prediction system can help identify customers who have a higher probability of leaving.

For this project, the ML problem is:

> Given customer information such as tenure, contract type, internet service, payment method, monthly charges, and other customer attributes, predict whether the customer is likely to churn.

The project intentionally prioritizes **recall** because missing a customer who is likely to churn can be more costly than incorrectly flagging a customer who ultimately stays.

---

# 🧭 Project Goals

[⬆️ Back to Table of Contents](#-table-of-contents)
The project was designed around several goals.

## Machine Learning

- Understand the customer churn dataset
- Build a preprocessing pipeline
- Train a classification model
- Evaluate the model
- Optimize the decision threshold toward churn recall
- Package the preprocessing and model together

## Software Engineering

- Separate training from serving
- Build a modular API
- Validate incoming requests
- Persist prediction history
- Add automated tests
- Containerize the application

## Deployment Engineering

- Run the application through Docker Compose
- Create a CI workflow with GitHub Actions
- Deploy the application to AWS EC2
- Put Nginx in front of FastAPI
- Back up the model artifact to S3
- Collect application logs with CloudWatch
- Verify the entire system through the public API

---

# 🏗️ System Architecture

[⬆️ Back to Table of Contents](#-table-of-contents)

## High-Level Architecture

    User / Client
          |
          v
    Public EC2 IP :80
          |
          v
        Nginx
    Reverse Proxy
          |
          v
    FastAPI Container
          |
    +-----+-----+-----+
    |           |     |
    v           v     v

/health /predict /explain
| |
v v
ML Pipeline SHAP
|
v
XGBoost Classifier
|
v
Prediction Result
|
v
PostgreSQL
Prediction History

             EC2 Instance
                  |
        +---------+---------+
        |                   |
        v                   v
      Docker          CloudWatch Agent
                            |
                            v
                      CloudWatch Logs

              S3
               |
               v
        churn_model.pkl
        Model Backup

---

# 🔄 End-to-End Flow

[⬆️ Back to Table of Contents](#-table-of-contents)
Customer Input
|
v
FastAPI
|
v
Pydantic Validation
|
v
Preprocessing Pipeline
|
v
XGBoost Model
|
v
Churn Probability
|
v
Decision Threshold
|
v
Prediction
|
+---+---+
| |
v v
PostgreSQL API Response
|
v
Prediction History

For explainability:

    Customer Input
          |
          v
    FastAPI /explain
          |
          v
    Preprocessing + Model
          |
          v
         SHAP
          |
          v
    Feature Contributions
          |
          v
    Explanation Response

---

# 📊 Dataset

[⬆️ Back to Table of Contents](#-table-of-contents)
The project uses the **Telco Customer Churn** dataset.

Dataset shape:

    7043 rows × 21 columns

The target variable is customer churn.

The dataset contains both categorical and numerical customer attributes.

Examples include:

- Gender
- Senior citizen status
- Partner
- Dependents
- Tenure
- Phone service
- Multiple lines
- Internet service
- Online security
- Online backup
- Device protection
- Tech support
- Streaming TV
- Streaming movies
- Contract
- Paperless billing
- Payment method
- Monthly charges
- Total charges

The original `customerID` column was removed because it is an identifier rather than a predictive feature.

---

# 🔍 Exploratory Data Analysis

[⬆️ Back to Table of Contents](#-table-of-contents)
Before modeling, the dataset was analyzed to understand:

- Dataset structure
- Feature types
- Target distribution
- Missing values
- Churn distribution
- Numerical feature behavior
- Categorical feature patterns
- Relationships between customer attributes and churn

One important data quality issue was discovered:

`TotalCharges` contained **11 missing values after numeric conversion**.

These values were handled during preprocessing.

EDA was used to understand the data before building the ML pipeline rather than immediately training a model.

---

# 🧹 Machine Learning Pipeline

[⬆️ Back to Table of Contents](#-table-of-contents)
The preprocessing pipeline was designed using scikit-learn.

The general flow is:

    Raw Data
       |
       +--> Remove customerID
       |
       +--> Convert TotalCharges
       |
       +--> Handle missing values
       |
       +--> Separate features and target
       |
       +--> Categorical preprocessing
       |
       +--> Numerical preprocessing
       |
       +--> Scaling
       |
       +--> Train/Test Split
       |
       v
    Preprocessing Pipeline
       |
       v
    XGBoost

## Important preprocessing principle

Training data is fitted using:

`fit_transform()`

while unseen/test data is processed using:

`transform()`

This prevents information from the test set from leaking into the training process.

---

# 🛠️ Feature Engineering

[⬆️ Back to Table of Contents](#-table-of-contents)
The existing dataset already contained useful customer attributes.

Rather than continuously creating additional features without a clear reason, the project deliberately kept feature engineering relatively simple.

The decision was:

> Use the existing features and focus on building a complete, reliable ML engineering system instead of endlessly engineering additional features.

This keeps the project focused on the complete ML lifecycle.

---

# 🤖 Model

[⬆️ Back to Table of Contents](#-table-of-contents)
The classification model used in this project is:

## XGBoost Classifier

XGBoost was selected because it is a strong tree-based algorithm for structured/tabular data and works well for binary classification problems.

The model was trained through the preprocessing pipeline.

The project also used class weighting to place greater emphasis on the churn class.

---

# 🎚️ Decision Threshold

[⬆️ Back to Table of Contents](#-table-of-contents)
Instead of relying blindly on the default classification threshold, the project uses a custom threshold:

    0.30

The model first produces a churn probability.

Conceptually:

    Model
      |
      v
    Churn Probability
      |
      v
    Compare with threshold = 0.30
      |
      +---- probability >= 0.30 ---> Churn
      |
      +---- probability <  0.30 ---> No Churn

This decision was made because the project prioritizes **recall for churn detection**.

---

# 🤖 Model Evaluation

[⬆️ Back to Table of Contents](#-table-of-contents)
The final model evaluation produced the following results:

| Metric    |  Value |
| --------- | -----: |
| Accuracy  | 0.6802 |
| Precision | 0.4477 |
| Recall    | 0.8690 |
| F1 Score  | 0.5909 |
| ROC-AUC   | 0.8247 |

The project intentionally prioritizes recall.

The final recall of `0.8690` means the model identifies a large proportion of actual churn cases.

The trade-off is lower precision, which is expected when the decision boundary is shifted toward detecting more potential churners.

---

# 🤖 Model Packaging

[⬆️ Back to Table of Contents](#-table-of-contents)
The trained model is stored as:

`models/churn_model.pkl`

The artifact contains the preprocessing pipeline together with the trained XGBoost model and the prediction threshold.

Conceptually:

    Saved Artifact
    {
        pipeline: preprocessing + XGBoost,
        threshold: 0.30
    }

This is important because the API should use the **same preprocessing logic that was used during training**.

The serving flow is therefore:

    Raw Customer Data
           |
           v
    Saved Pipeline
           |
           v
    Preprocessing
           |
           v
    XGBoost
           |
           v
    Probability
           |
           v
    Threshold
           |
           v
    Prediction

Training and API serving are kept separate.

---

# ⚡ FastAPI Application

[⬆️ Back to Table of Contents](#-table-of-contents)

> 🚦 **The ML model becomes a service here.** Instead of manually opening a notebook and running inference, another system can send an HTTP request and receive a structured prediction.

The trained ML pipeline is exposed through a FastAPI application.

The API provides three core endpoints:

    GET  /health
    POST /predict
    POST /explain

FastAPI is responsible for:

- Receiving requests
- Validating input
- Calling the prediction service
- Calling the explanation service
- Returning structured responses
- Handling invalid requests

---

# 🔌 API Endpoints

[⬆️ Back to Table of Contents](#-table-of-contents)

## 1. Health Check

    GET /health

Purpose:

Determine whether the API service is alive and responding.

Example response:

    {
      "status": "healthy"
    }

---

## 2. Prediction

    POST /predict

Purpose:

Predict customer churn and store the prediction in the database.

The request contains customer information.

Example:

    {
      "gender": "Female",
      "SeniorCitizen": 0,
      "Partner": "Yes",
      "Dependents": "No",
      "tenure": 24,
      "PhoneService": "Yes",
      "MultipleLines": "No",
      "InternetService": "Fiber optic",
      "OnlineSecurity": "No",
      "OnlineBackup": "Yes",
      "DeviceProtection": "No",
      "TechSupport": "No",
      "StreamingTV": "Yes",
      "StreamingMovies": "Yes",
      "Contract": "Month-to-month",
      "PaperlessBilling": "Yes",
      "PaymentMethod": "Electronic check",
      "MonthlyCharges": 89.95,
      "TotalCharges": 2150.50
    }

Example response from the deployed system:

    {
      "churn_prediction": 1,
      "churn_probability": 0.7442374229431152,
      "risk_level": "High"
    }

---

## 3. Explain Prediction

    POST /explain

Purpose:

Generate the churn prediction and explain the prediction using SHAP.

The response contains:

- Churn prediction
- Churn probability
- Risk level
- Feature-level explanation
- SHAP values
- Feature impact

Example structure:

    {
      "churn_prediction": 1,
      "churn_probability": 0.7442374229431152,
      "risk_level": "High",
      "explanation": [
        {
          "feature": "cat__Contract_Month-to-month",
          "shap_value": 0.69,
          "impact": "increases_churn"
        }
      ]
    }

---

# 🛡️ API Validation

[⬆️ Back to Table of Contents](#-table-of-contents)
Incoming requests are validated using Pydantic.

For example, `gender` only accepts:

    Male
    Female

An invalid request such as:

    {
      "gender": "InvalidGender"
    }

is rejected with a validation error.

The deployed API returned:

    422 Unprocessable Entity

This demonstrates that invalid inputs are rejected before reaching the prediction logic.

---

# 🔎 SHAP Explainability

[⬆️ Back to Table of Contents](#-table-of-contents)
The `/explain` endpoint uses SHAP to provide feature-level explanations for model predictions.

The goal is to move from:

    Customer
       |
       v
    Prediction = Churn

to:

    Customer
       |
       v
    Prediction = Churn
       |
       +--> Which features influenced the prediction?
       |
       +--> How strongly did they influence it?
       |
       +--> Did they increase or decrease churn?

This makes the model output easier to interpret.

---

# 🗄️ Database

[⬆️ Back to Table of Contents](#-table-of-contents)
The application stores prediction history in PostgreSQL.

The database has a practical purpose:

> Store historical predictions generated by the API.

The prediction flow is:

    POST /predict
          |
          v
    ML Prediction
          |
          v
    Save Prediction
          |
          v
    Return API Response

Stored information includes:

- Prediction ID
- Churn prediction
- Churn probability
- Risk level
- Creation timestamp

Example database records generated during deployment testing:

    id | churn_prediction | churn_probability     | risk_level | created_at
    ---+------------------+----------------------+------------+----------------------------
     2 | 1                | 0.7442374229431152   | High       | ...
     1 | 0                | 0.07769378274679184  | Low        | ...

The probability stored in PostgreSQL matched the probability returned by the public API.

This verified that the API prediction and database persistence were connected correctly.

---

# 🔧 SQLAlchemy

[⬆️ Back to Table of Contents](#-table-of-contents)
SQLAlchemy is used as the database interaction layer.

The application uses:

- Database engine
- Session management
- Database model
- CRUD operations
- Prediction persistence

This keeps database interaction separate from the core prediction logic.

---

# 🧪 Testing

[⬆️ Back to Table of Contents](#-table-of-contents)
The application includes automated testing using `pytest`.

Testing covers important application behavior such as:

- Application startup
- Valid requests
- Invalid requests
- Missing fields
- Invalid categorical values
- Prediction responses
- Database logging
- Failure cases

The objective is to make application behavior repeatable and automatically verifiable rather than relying entirely on manual testing.

---

# 🐳 Docker

[⬆️ Back to Table of Contents](#-table-of-contents)

> 📦 **Goal:** make the application portable. The same containerized application can be run locally and on the EC2 instance without rebuilding the runtime environment from scratch.

The FastAPI application is containerized using Docker.

Conceptually:

    Docker Image
         |
         v
    FastAPI Container
         |
         v
       Uvicorn
         |
         v
    FastAPI Application

Docker provides:

- Consistent runtime environment
- Isolated application environment
- Reproducible deployment
- Easier local/cloud execution

---

# 🐳 Docker Compose

[⬆️ Back to Table of Contents](#-table-of-contents)
Docker Compose is used to run the application and database together.

Architecture:

    Docker Compose
          |
          +------------------+
          |                  |
          v                  v
    FastAPI Container   PostgreSQL Container

The two services communicate through the Docker network.

The application container exposes the API while PostgreSQL provides prediction storage.

Typical command:

    docker compose up --build

To inspect running services:

    docker compose ps

Example deployed services:

    customer-churn-api
    customer-churn-db

---

# 🔄 CI/CD

[⬆️ Back to Table of Contents](#-table-of-contents)
GitHub Actions is used for basic continuous integration.

The CI workflow performs checks such as:

    GitHub Push / Pull Request
              |
              v
    Install Dependencies
              |
              v
         Run Tests
              |
              v
    Build Docker Image
              |
              v
       Workflow Success

The purpose of the CI pipeline is to automatically verify that changes do not break the application and that the Docker image can be built successfully.

---

# ☁️ AWS Deployment

[⬆️ Back to Table of Contents](#-table-of-contents)

> 💡 **AWS was used as a temporary learning environment, not as a permanent production platform.**

The application was temporarily deployed to AWS for learning, verification, and portfolio demonstration.

The deployment architecture was intentionally kept simple.

No unnecessary infrastructure such as:

- Kubernetes
- Load Balancers
- NAT Gateway
- RDS
- GPU instances
- Microservices
- Permanent domain infrastructure

was introduced.

The deployment flow was:

    Internet
       |
       v
      EC2
       |
       v
     Nginx
       |
       v
     Docker
       |
       v
    FastAPI
       |
       +------> PostgreSQL
       |
       +------> ML Pipeline

---

# 💻 EC2

[⬆️ Back to Table of Contents](#-table-of-contents)
Amazon EC2 was used to host the Dockerized application.

The EC2 instance provided the compute environment required to run:

- Docker
- FastAPI container
- PostgreSQL container
- Nginx
- CloudWatch Agent

SSH was used to administer the instance.

Example:

    ssh -i customer-churn-key.pem ec2-user@<EC2_PUBLIC_IP>

The EC2 Security Group allowed the required traffic for:

- SSH administration
- HTTP access through Nginx

The application was accessed publicly through Nginx rather than directly exposing FastAPI as the public API entry point.

---

# 🔐 IAM

[⬆️ Back to Table of Contents](#-table-of-contents)
An IAM role was attached to the EC2 instance to allow the instance to interact with AWS services without embedding AWS access keys inside the application.

The role was used for:

- S3 model backup access
- CloudWatch Agent log publishing

The S3 permissions were kept scoped to the required bucket/object operations rather than granting unnecessary account-wide S3 permissions.

---

# 🌐 Nginx

[⬆️ Back to Table of Contents](#-table-of-contents)
Nginx was used as a reverse proxy in front of FastAPI.

The public architecture is:

    Internet
       |
       v
    EC2 :80
       |
       v
    Nginx
       |
       v
    FastAPI :8000

FastAPI runs inside Docker while Nginx receives public HTTP traffic.

This demonstrates the common reverse-proxy architecture used when an application server sits behind a web server.

The public `/health` endpoint was successfully tested through Nginx.

---

# 🪣 S3 Model Backup

[⬆️ Back to Table of Contents](#-table-of-contents)
Amazon S3 was used specifically as **model artifact backup/storage**.

The trained model artifact:

    churn_model.pkl

was uploaded to an S3 bucket.

The S3 bucket contained:

    churn_model.pkl

with a size of approximately:

    442 KB

The objective was not to redesign model serving around S3.

Instead:

    EC2
     |
     | running application
     |
     +--------------------+
                          |
                          v
                         S3
                          |
                          v
                   Model Backup

---

# ♻️ S3 Restore Verification

[⬆️ Back to Table of Contents](#-table-of-contents)
The model was downloaded from S3 back to the EC2 instance.

Example:

    aws s3 cp     s3://<BUCKET_NAME>/churn_model.pkl     /tmp/churn_model_restore.pkl

The restored file was approximately:

    442K

The SHA-256 checksum was also verified.

Both downloaded copies produced the same checksum:

    47487e09a3302a9abf7dbb12a4eaccf3e19f52d27da6975ed198f39cd7c96cd4

This verified that the model artifact could be restored from S3 without corruption.

---

# 📡 CloudWatch

[⬆️ Back to Table of Contents](#-table-of-contents)

> 👀 **Monitoring objective:** make application activity visible outside the container so requests and failures can be inspected centrally.

Amazon CloudWatch was used for basic application logging and monitoring.

The CloudWatch Agent was installed on the EC2 instance.

Docker application logs were collected into CloudWatch.

CloudWatch captured application requests including:

    GET /health       → 200 OK
    GET /docs         → 200 OK
    GET /openapi.json → 200 OK
    POST /predict     → 200 OK
    POST /explain     → 200 OK
    POST /predict     → 422 Unprocessable Entity

This demonstrated that both successful API requests and validation failures were visible through centralized cloud logging.

The project intentionally avoided unnecessary expensive monitoring infrastructure.

---

# 🌍 Public Deployment Flow

[⬆️ Back to Table of Contents](#-table-of-contents)
The final public request flow was:

    Windows / External Client
              |
              v
    Public EC2 IP :80
              |
              v
        Security Group
              |
              v
             Nginx
              |
              v
    FastAPI Docker Container
              |
              +------------------+
              |                  |
              v                  v
           ML Model          PostgreSQL
              |
              +-------> Prediction
              |
              +-------> SHAP Explanation

---

# ✅ Public API Verification

[⬆️ Back to Table of Contents](#-table-of-contents)
The public API was verified through the EC2 public IP.

## Health

    GET /health

Response:

    {
      "status": "healthy"
    }

## Prediction

A real customer request was sent to:

    POST /predict

The deployed system returned:

    churn_prediction = 1
    churn_probability = 0.7442374229431152
    risk_level = High

## Explanation

The same customer was sent to:

    POST /explain

The API returned the prediction together with SHAP-based feature explanations.

## Invalid request

An invalid categorical value was deliberately sent to `/predict`.

The API correctly returned:

    422 Unprocessable Entity

This verified public request validation.

---

# 🏁 Deployment Verification

[⬆️ Back to Table of Contents](#-table-of-contents)
The final public deployment successfully verified:

| Component                     | Verification |
| ----------------------------- | ------------ |
| Public `/health`              | ✅           |
| Public `/predict`             | ✅           |
| Public `/explain`             | ✅           |
| Pydantic validation           | ✅           |
| PostgreSQL prediction logging | ✅           |
| Docker containers             | ✅           |
| Docker Compose                | ✅           |
| Nginx reverse proxy           | ✅           |
| S3 model backup               | ✅           |
| S3 model restore              | ✅           |
| SHA-256 integrity             | ✅           |
| CloudWatch logs               | ✅           |
| Successful request logging    | ✅           |
| Error request logging         | ✅           |

---

# 📁 Project Structure

[⬆️ Back to Table of Contents](#-table-of-contents)
The project follows a modular structure separating training, API serving, database interaction, configuration, and infrastructure concerns.

A simplified representation is:

    customer-churn-ml-system/
    │
    ├── src/
    │   ├── api/
    │   │   ├── main.py
    │   │   └── ...
    │   │
    │   ├── ...
    │   │
    │   └── ...
    │
    ├── models/
    │   └── churn_model.pkl
    │
    ├── tests/
    │   └── ...
    │
    ├── train.py
    ├── config.yaml
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── requirements-dev.txt
    ├── .github/
    │   └── workflows/
    │       └── ...
    │
    └── README.md

The exact repository structure may contain additional modules and configuration files.

---

# 💻 Local Setup

[⬆️ Back to Table of Contents](#-table-of-contents)

## 1. Clone the repository

    git clone <YOUR_GITHUB_REPOSITORY_URL>
    cd customer-churn-ml-system

## 2. Create a virtual environment

Windows:

    python -m venv .venv
    .venv\Scripts\activate

Linux/macOS:

    python3 -m venv .venv
    source .venv/bin/activate

## 3. Install dependencies

    pip install -r requirements.txt

For development/testing dependencies:

    pip install -r requirements-dev.txt

## 4. Configure the environment

Create the required environment configuration used by the application.

Secrets and environment-specific values should not be committed to Git.

---

# 🏋️ Training the Model

[⬆️ Back to Table of Contents](#-table-of-contents)
The project uses a root-level training script:

    python train.py

The training process:

    Dataset
       |
       v
    Preprocessing
       |
       v
    Train/Test Split
       |
       v
    XGBoost
       |
       v
    Evaluation
       |
       v
    churn_model.pkl

The resulting model artifact is stored under:

    models/churn_model.pkl

---

# ▶️ Running the Application

[⬆️ Back to Table of Contents](#-table-of-contents)
The FastAPI application can be started using Uvicorn.

The deployed application uses:

    uvicorn src.api.main:app

The API exposes:

    GET  /health
    POST /predict
    POST /explain

Swagger documentation is available at:

    /docs

OpenAPI specification:

    /openapi.json

---

# 🐳 Running with Docker Compose

[⬆️ Back to Table of Contents](#-table-of-contents)
Build and start the application stack:

    docker compose up --build

Check running services:

    docker compose ps

Expected architecture:

    customer-churn-api
    customer-churn-db

Stop the stack:

    docker compose down

---

# 🧪 Running Tests

[⬆️ Back to Table of Contents](#-table-of-contents)
Run the automated test suite using:

    pytest

The tests are intended to verify application behavior including:

- API behavior
- Request validation
- Prediction logic
- Database persistence
- Important failure cases
- Explanation functionality

---

# 🧾 Example Prediction

[⬆️ Back to Table of Contents](#-table-of-contents)
Example customer:

    {
      "gender": "Female",
      "SeniorCitizen": 0,
      "Partner": "Yes",
      "Dependents": "No",
      "tenure": 24,
      "PhoneService": "Yes",
      "MultipleLines": "No",
      "InternetService": "Fiber optic",
      "OnlineSecurity": "No",
      "OnlineBackup": "Yes",
      "DeviceProtection": "No",
      "TechSupport": "No",
      "StreamingTV": "Yes",
      "StreamingMovies": "Yes",
      "Contract": "Month-to-month",
      "PaperlessBilling": "Yes",
      "PaymentMethod": "Electronic check",
      "MonthlyCharges": 89.95,
      "TotalCharges": 2150.50
    }

Example result from the deployed model:

    {
      "churn_prediction": 1,
      "churn_probability": 0.7442374229431152,
      "risk_level": "High"
    }

Interpretation:

    Prediction:
    Customer is classified as likely to churn.

    Probability:
    Approximately 74.42% churn probability.

    Risk:
    High

---

# 🔎 Example Explanation

[⬆️ Back to Table of Contents](#-table-of-contents)
The `/explain` endpoint returns SHAP-based explanations.

Example response structure:

    {
      "churn_prediction": 1,
      "churn_probability": 0.7442374229431152,
      "risk_level": "High",
      "explanation": [
        {
          "feature": "cat__Contract_Month-to-month",
          "shap_value": 0.6907002925872803,
          "impact": "increases_churn"
        }
      ]
    }

The explanation contains the features that contributed to the model's prediction and whether their contribution increased or decreased the predicted churn risk.

---

# ☁️ Deployment Commands Used During AWS Testing

[⬆️ Back to Table of Contents](#-table-of-contents)
After connecting to EC2:

    ssh -i customer-churn-key.pem ec2-user@<EC2_PUBLIC_IP>

Check containers:

    docker compose ps

Check API logs:

    docker logs --tail 30 customer-churn-api

Check Nginx:

    sudo systemctl status nginx

Check CloudWatch Agent:

    sudo systemctl status amazon-cloudwatch-agent

Check S3 model:

    aws s3 ls s3://<BUCKET_NAME>/

Download the model:

    aws s3 cp     s3://<BUCKET_NAME>/churn_model.pkl     /tmp/churn_model_restore.pkl

Verify the restored artifact:

    sha256sum /tmp/churn_model_restore.pkl

---

# 🧠 Key Engineering Decisions

[⬆️ Back to Table of Contents](#-table-of-contents)

## 1. Recall over accuracy

The project deliberately prioritizes churn recall.

A churn prediction system that misses too many actual churners may be less useful than one that generates some additional false positives.

This is why the model uses class weighting and a lower decision threshold.

## 2. Pipeline-based model packaging

Preprocessing and the model are packaged together.

This prevents the API from accidentally applying different preprocessing logic from the training pipeline.

    Raw Input
       |
       v
    Saved Pipeline
       |
       +--> Preprocessing
       |
       +--> XGBoost
       |
       v
    Prediction

## 3. PostgreSQL for prediction history

The database exists for a concrete reason:

> Store prediction history.

The project does not introduce a database merely to add another technology.

## 4. Docker Compose instead of unnecessary orchestration

The system only needs two main services:

    FastAPI
    PostgreSQL

Docker Compose is sufficient for this architecture.

Kubernetes and microservices would add complexity without improving the learning objective of this project.

## 5. S3 as model backup

S3 is used as an artifact backup rather than turning the entire model-serving architecture into an S3-dependent system.

The running API continues to use its deployed model artifact.

S3 provides a backup copy.

## 6. Nginx as reverse proxy

Nginx provides the public HTTP entry point while FastAPI remains behind it.

    Public :80
        |
        v
      Nginx
        |
        v
    FastAPI :8000

## 7. Temporary AWS deployment

The AWS deployment exists for:

- Learning
- Deployment practice
- Public verification
- Portfolio demonstration

It is not intended to run permanently.

After the demonstration, unnecessary AWS resources are removed to avoid ongoing costs.

---

# 💰 AWS Cost and Security Considerations

[⬆️ Back to Table of Contents](#-table-of-contents)
The project was designed with cost safety in mind.

The following infrastructure was intentionally avoided:

- GPU instances
- NAT Gateway
- Load Balancer
- RDS solely for the sake of using RDS
- Kubernetes
- Large EC2 instances
- Unnecessary Elastic IP usage
- Expensive monitoring infrastructure
- Paid domain infrastructure

The AWS deployment was kept intentionally small.

---

# 🔐 IAM Security

[⬆️ Back to Table of Contents](#-table-of-contents)
The EC2 instance used an IAM role instead of hardcoding AWS credentials into the application.

The role provided the permissions needed for:

- S3 model backup access
- CloudWatch Agent logging

The role was intentionally not granted unnecessary account-wide permissions.

For example, attempting:

    aws s3 ls

from EC2 attempted to list all buckets and was denied because the role did not have:

    s3:ListAllMyBuckets

This was expected.

The role could instead access the specific model backup bucket:

    aws s3 ls s3://<BUCKET_NAME>/

This demonstrates the principle of granting only the permissions required for the task.

---

# 🌍 Public Testing

[⬆️ Back to Table of Contents](#-table-of-contents)
The final application was tested from outside the EC2 instance.

The public flow was:

    External Client
          |
          v
    EC2 Public IP
          |
          v
    Security Group
          |
          v
        Nginx
          |
          v
       FastAPI
          |
          +--------> ML Pipeline
          |
          +--------> PostgreSQL

The public tests verified:

- Health endpoint
- Swagger documentation
- OpenAPI specification
- Prediction
- SHAP explanation
- Invalid input handling
- Database persistence

The public `/predict` response was compared with the corresponding database record to verify that the same prediction was persisted.

---

# 📡 Monitoring Verification

[⬆️ Back to Table of Contents](#-table-of-contents)
CloudWatch received the application's Docker logs.

The following types of events were visible:

    GET /health       → 200 OK
    GET /docs         → 200 OK
    GET /openapi.json → 200 OK
    POST /predict     → 200 OK
    POST /explain     → 200 OK
    POST /predict     → 422 Unprocessable Entity

This verified that the monitoring setup could capture both successful requests and application validation errors.

---

# 🎓 What I Learned

[⬆️ Back to Table of Contents](#-table-of-contents)
This project was primarily built to understand the complete ML engineering lifecycle.

The most important lessons were:

## Machine Learning

- EDA should happen before modeling
- Data leakage must be prevented
- Preprocessing must be reproducible
- Model performance must be evaluated using multiple metrics
- Accuracy alone is not enough for imbalanced classification
- Decision thresholds can change the precision/recall trade-off

## ML Engineering

- A trained model is only one part of an ML system
- Training and serving should be separated
- Model artifacts need reliable packaging
- APIs need validation
- Predictions may need persistence
- Explainability can be added through SHAP

## Software Engineering

- Application logic should be modular
- Database interaction should be separated from API logic
- Automated tests provide repeatable verification
- Docker provides reproducible environments
- Docker Compose simplifies multi-service development

## 🔄 CI/CD

- Code changes can automatically trigger tests
- Docker builds can be verified automatically
- CI catches problems before deployment

## Cloud

- EC2 provides compute for the application
- Security Groups control network access
- IAM roles provide AWS permissions without embedding credentials
- S3 can store model artifacts
- CloudWatch can centralize application logs
- Nginx can act as a reverse proxy

## Deployment

The most important lesson was that:

> Building an ML model and deploying an ML system are two very different tasks.

The project helped connect the entire lifecycle:

    Data
     ↓
    Model
     ↓
    API
     ↓
    Database
     ↓
    Tests
     ↓
    Docker
     ↓
    CI
     ↓
    Cloud
     ↓
    Monitoring

---

# ⚠️ Limitations

[⬆️ Back to Table of Contents](#-table-of-contents)
This project is intentionally a learning and portfolio system rather than a commercial production platform.

It does not include:

- Kubernetes
- Microservices
- Distributed inference
- GPU infrastructure
- Load balancing
- Auto-scaling
- Managed RDS
- Redis
- Kafka
- Celery
- MLflow
- Feature stores
- Complex model serving platforms
- Permanent domain infrastructure

These technologies can be valuable in larger systems, but adding them here would increase complexity without being necessary for the project's learning objectives.

---

# 🚀 Future Improvements

[⬆️ Back to Table of Contents](#-table-of-contents)
If this system were extended beyond the current learning objective, possible improvements could include:

- Model versioning
- Automated model retraining
- Data drift detection
- Model monitoring
- Authentication and authorization
- Rate limiting
- HTTPS with a production domain
- Managed database infrastructure
- Automated cloud deployment
- Infrastructure as Code
- Horizontal scaling
- More advanced CI/CD
- Model registry
- Experiment tracking

These are intentionally outside the current project's scope.

---

# 🏆 Project Outcome

[⬆️ Back to Table of Contents](#-table-of-contents)

> 🎉 **The final outcome is a complete ML engineering workflow, not just a trained model.**

This project demonstrates an end-to-end Machine Learning Engineering workflow.

The final system connects:

    Data
     ↓
    EDA
     ↓
    Preprocessing
     ↓
    XGBoost
     ↓
    Model Evaluation
     ↓
    Model Packaging
     ↓
    FastAPI
     ↓
    PostgreSQL
     ↓
    Automated Testing
     ↓
    Docker
     ↓
    Docker Compose
     ↓
    GitHub Actions
     ↓
    AWS EC2
     ↓
    Nginx
     ↓
    S3
     ↓
    CloudWatch
     ↓
    Public API

The deployed API was successfully tested from outside the EC2 instance.

The system successfully performed:

- Public health checks
- Real churn predictions
- SHAP explanations
- Database persistence
- Invalid request handling
- Dockerized execution
- S3 model backup and restoration
- CloudWatch application logging

The model achieved:

    Accuracy  : 0.6802
    Precision : 0.4477
    Recall    : 0.8690
    F1        : 0.5909
    ROC-AUC   : 0.8247

The project demonstrates not only how to train a machine learning model, but how to turn that model into a complete, testable, containerized, monitored, and temporarily cloud-deployed ML application.

---

# 🗺️ Complete Project Lifecycle

[⬆️ Back to Table of Contents](#-table-of-contents)
📊 DATA
↓
🔍 EDA
↓
🧹 PREPROCESSING
↓
🤖 XGBOOST
↓
📈 EVALUATION
↓
📦 MODEL ARTIFACT
↓
⚡ FASTAPI
↓
🗄️ POSTGRESQL
↓
🧪 TESTS
↓
🐳 DOCKER
↓
🔗 DOCKER COMPOSE
↓
🔄 GITHUB ACTIONS
↓
☁️ AWS EC2
↓
🌐 NGINX
↓
🪣 S3 BACKUP
↓
📡 CLOUDWATCH
↓
🌍 PUBLIC VERIFICATION
↓
🎥 DEMONSTRATION
↓
🧹 AWS CLEANUP

> **Build → Test → Deploy → Verify → Demonstrate → Clean Up**

---

# 🏗️ Final Architecture

[⬆️ Back to Table of Contents](#-table-of-contents)
+-----------------------+
| External Client |
+-----------+-----------+
|
v
+-----------------------+
| EC2 Public IP |
| :80 |
+-----------+-----------+
|
v
+-----------------------+
| Nginx |
| Reverse Proxy |
+-----------+-----------+
|
v
+--------------------------------------+
| FastAPI Container |
| |
| /health /predict /explain |
+------------------+-------------------+
|
+------------+------------+
| | |
v v v
PostgreSQL ML Pipeline SHAP
| | |
| v |
| XGBoost |
| | |
| v |
| Churn Probability |
| | |
| v |
| Threshold |
| | |
+------------+------------+
|
v
Prediction Response

    +------------------+       +--------------------+
    |       S3         |       |    CloudWatch      |
    |                  |       |                    |
    | churn_model.pkl  |       | Application Logs   |
    | Model Backup     |       | Request/Error Logs |
    +------------------+       +--------------------+

---

## Built as a learning project

The primary objective of this project was not to build the most complex infrastructure possible.

It was to understand the complete journey of an ML model:

> **From a dataset in development to a tested, containerized, cloud-deployed, monitored ML API.**

**Build → Test → Deploy → Verify → Demonstrate → Clean Up**

---

## ⭐ Final Note

This repository is a record of the complete learning journey from **ML experimentation to cloud-deployed ML engineering**.

> **One model. One system. Complete lifecycle.** 🚀
