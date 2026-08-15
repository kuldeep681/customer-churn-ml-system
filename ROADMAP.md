\# 🔒 CUSTOMER CHURN ML SYSTEM — LOCKED MASTER ROADMAP

\## Project Goal

Build one complete **\*\*end-to-end Machine Learning Engineering system\*\***:

_>_ **\*\*Data → ML → Model → API → Database → Testing → Docker → CI/CD → AWS → Nginx → S3 → CloudWatch → Public Demo → Cleanup\*\***

This is a **\*\*learning + portfolio project\*\***.

We are **\*\*not\*\*** trying to build a commercially productionized platform.

We will:

**\*\*Build → test → deploy once → demonstrate → record/screenshots → shut down AWS resources.\*\***

No unnecessary frontend, Kubernetes, microservices, GPU, RDS, load balancer, domain, or other complexity.

**---**

\# PHASE 0 — FOUNDATIONS ✅

\### Objective

Understand what we are building before implementation.

\### Completed

\- [x] Understand customer churn problem
\- [x] Understand classification
\- [x] Understand why recall matters for churn
\- [x] Understand AWS/free-tier cost concerns
\- [x] Design overall architecture
\- [x] Understand ML → API → deployment flow

\### Exit condition

We understand the system we're going to build.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 1 — PROJECT SETUP ✅

\### Objective

Create a clean, modular project structure.

\### Completed

\- [x] Project folder structure
\- [x] Configuration system
\- [x] \`config.yaml\`
\- [x] Configuration loader
\- [x] Environment setup
\- [x] Logging foundation
\- [x] Runtime/development requirements separation

\### Exit condition

Project can be organized and configured without hardcoded paths.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 2 — EDA ✅

\### Objective

Understand the dataset before modeling.

Dataset:

**\*\*Telco Customer Churn\*\***

Shape:

**\*\*7043 × 21\*\***

\### Completed

\- [x] Load dataset
\- [x] Inspect shape
\- [x] Inspect columns
\- [x] Understand target
\- [x] Understand categorical features
\- [x] Understand numerical features
\- [x] Check missing values
\- [x] Analyze churn distribution
\- [x] Visualizations
\- [x] Understand important patterns

Important discovery:

\`TotalCharges\` contained 11 missing values after numeric conversion.

\### Exit condition

We understand the dataset and what preprocessing is required.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 3 — DATA PIPELINE ✅

\### Objective

Convert raw customer data into model-ready data.

\### Completed

\- [x] Remove \`customerID\`
\- [x] Convert \`TotalCharges\`
\- [x] Handle missing values
\- [x] Separate X and y
\- [x] Encode categorical features
\- [x] Process numerical features
\- [x] Scaling
\- [x] Train/test split
\- [x] Prevent data leakage
\- [x] Build sklearn preprocessing pipeline

Important mental model:

_> Training data → \`fit_transform()\`_
_> Test data → \`transform()\`_

\### Exit condition

Raw data can reliably enter the preprocessing pipeline.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 4 — FEATURE ENGINEERING ✅

\### Objective

Determine whether additional feature engineering is necessary.

\### Completed

\- [x] Review existing features
\- [x] Basic feature processing
\- [x] Evaluate need for transformations
\- [x] Decide that aggressive additional feature engineering is unnecessary

\### Important decision

We are **\*\*not endlessly engineering features just because we can\*\***.

The current dataset/features are sufficient for the learning objective.

\### Exit condition

Feature engineering decision is justified.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 5 — MODEL TRAINING ✅

\### Objective

Train the churn prediction model.

\### Model

**\*\*XGBoost Classifier\*\***

\### Completed

\- [x] Train XGBoost
\- [x] Configure class weighting
\- [x] Train model through preprocessing pipeline
\- [x] Save trained artifact
\- [x] Create root-level \`train.py\`
\- [x] Separate training from API serving

Current artifact:

\`\`\`text
models/churn_model.pkl
\`\`\`

Current artifact concept:

\`\`\`text
{
    "pipeline": preprocessing + XGBoost,
    "threshold": 0.3
}
\`\`\`

\### Important locked decision

**\*\*No further model tuning/balancing for now.\*\***

We already deliberately optimized toward recall.

\### Exit condition

A reproducible training process generates the saved model.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 6 — MODEL EVALUATION ✅

\### Objective

Evaluate whether the model works.

\### Completed

\- [x] Accuracy
\- [x] Precision
\- [x] Recall
\- [x] F1
\- [x] ROC-AUC
\- [x] Confusion matrix
\- [x] Cross-validation recall

Current final result:

\| Metric    |  Value |
\| --------- | -----: |
\| Accuracy  | 0.6802 |
\| Precision | 0.4477 |
\| Recall    | 0.8690 |
\| F1        | 0.5909 |
\| ROC-AUC   | 0.8247 |

\### Exit condition

Model performance is understood and documented.

**\*\*STATUS: COMPLETE\*\***

**---**

\# PHASE 7 — MODEL PACKAGING ⚠️

\### Objective

Make the trained model usable by the application.

\### Intended architecture

\`\`\`text
Raw customer data
        ↓
Saved Pipeline
        ↓
Preprocessing
        ↓
XGBoost
        ↓
Probability
        ↓
Threshold
        ↓
Prediction
\`\`\`

\### Completed conceptually

\- [x] Model loader concept
\- [x] Prediction logic concept
\- [x] Pipeline packaging
\- [x] Threshold saved
\- [x] \`churn_model.pkl\` created

\### Remaining

\- [x] Synchronize API/model-loading code with the current pipeline artifact
\- [ ] Ensure \`model_loader.py\`
\- [x] Ensure prediction service
\- [x] Ensure prediction endpoint
\- [ ] Verify everything uses \`pipeline + threshold\`
\- [x] Run complete regression test

\### Exit condition

The application correctly loads the **\*\*current pipeline-based model artifact\*\***.

**\*\*STATUS: ALMOST COMPLETE — FIRST THING TO FIX\*\***

**---**

\# PHASE 8 — FASTAPI APPLICATION ⚠️

\### Objective

Expose the ML system through an API.

\### Already completed

\- [x] FastAPI setup
\- [x] \`/predict\`
\- [x] Pydantic request schema
\- [x] Pydantic validation
\- [x] Prediction response
\- [x] Risk level
\- [x] Invalid input testing

Current API:

\`\`\`text
POST /predict
\`\`\`

\### Still required

\#### \`/health\`

\`\`\`text
GET /health
\`\`\`

Purpose:

Determine whether the service is alive and able to serve requests.

\#### \`/explain\`

\`\`\`text
POST /explain
\`\`\`

Purpose:

Use **\*\*SHAP\*\*** to explain why the model produced a prediction.

\### Locked API

\`\`\`text
POST /predict
GET  /health
POST /explain
\`\`\`

No unnecessary endpoints.

\### Exit condition

All three endpoints work correctly.

**\*\*STATUS: PARTIALLY COMPLETE\*\***

**---**

\# PHASE 9 — DATABASE + SQLALCHEMY ❌

\### Objective

Learn how an ML API interacts with a database.

The database has a **\*\*real purpose\*\***:

_> Store prediction history._

Flow:

\`\`\`text
POST /predict
      ↓
Model prediction
      ↓
Store prediction
      ↓
Return response
\`\`\`

\### Implement

\- [x] SQLAlchemy
\- [x] Database model
\- [x] Database engine
\- [x] Session management
\- [x] Database initialization
\- [x] CRUD basics
\- [x] Prediction logging
\- [x] Request data
\- [x] Prediction
\- [x] Probability
\- [x] Risk level
\- [x] Timestamp

\### Database decision

Use a lightweight/local database during development rather than immediately introducing expensive AWS infrastructure.

We will decide the deployment database strategy later based on cost and learning requirements.

\### Exit condition

A prediction is successfully saved and retrieved.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 10 — AUTOMATED TESTING ❌

\### Objective

Make sure the application can automatically verify itself.

\### Implement

\- [x] Test API startup
\- [ ] Test \`/health\`
\- [ ] Test \`/predict\`
\- [x] Test valid request
\- [x] Test invalid request
\- [x] Test missing fields
\- [x] Test invalid categorical values
\- [x] Test prediction response
\- [x] Test database logging
\- [ ] Test \`/explain\`
\- [x] Test important failure cases

Use a proper testing framework such as \`pytest\`.

\### Exit condition

Running tests automatically verifies the application.

\`\`\`text
pytest
\`\`\`

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 11 — DOCKER ❌

\### Objective

Learn containerization.

\### Learn

\- [x] What is an image?
\- [x] What is a container?
\- [x] Dockerfile
\- [x] Build image
\- [x] Run container
\- [x] Environment variables
\- [x] Volumes
\- [x] Networks
\- [x] Port mapping
\- [x] Container logs
\- [x] Stop/remove containers

\### Implement

\`\`\`text
Dockerfile
\`\`\`

Application should run inside a container.

\### Exit condition

FastAPI application runs successfully inside Docker.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 12 — DOCKER COMPOSE ❌

\### Objective

Learn multi-service orchestration.

Target conceptual architecture:

\`\`\`text
Docker Compose
      │
      ├── FastAPI
      │
      └── Database
\`\`\`

\### Implement

\- [ ] \`docker-compose.yml\`
\- [x] FastAPI service
\- [x] Database service
\- [x] Environment variables
\- [x] Service communication
\- [x] Volumes
\- [x] Networking
\- [x] Startup/shutdown behavior

Run:

\`\`\`text
docker compose up --build
\`\`\`

\### Exit condition

Entire local application stack runs through Compose.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 13 — GITHUB ACTIONS / CI ❌

\### Objective

Learn basic CI/CD.

Pipeline:

\`\`\`text
GitHub
   ↓
GitHub Actions
   ↓
Install dependencies
   ↓
Run tests
   ↓
Build Docker image
\`\`\`

\### Implement

\- [x] Workflow file
\- [x] Trigger on push
\- [x] Trigger on pull request
\- [x] Install dependencies
\- [x] Run tests
\- [x] Build Docker image
\- [x] Verify workflow succeeds

\### Exit condition

A GitHub push/PR automatically runs the project's checks.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 14 — AWS FUNDAMENTALS + COST SAFETY ❌

\### Objective

Understand AWS **\*\*before spending money/resources\*\***.

\### Learn

\- [ ] IAM
\- [ ] IAM users/roles basics
\- [ ] MFA
\- [ ] EC2
\- [ ] S3
\- [ ] VPC basics
\- [ ] Security Groups
\- [ ] CloudWatch
\- [ ] Billing
\- [ ] Free-tier/credit rules applicable to the account
\- [ ] Cost monitoring
\- [ ] Resource cleanup

\### Critical rule

Before creating AWS resources:

**\*\*We verify the current AWS pricing/free-tier/credit conditions.\*\***

We do **\*\*not\*\*** assume old tutorial rules.

\### Avoid

\- [ ] GPU
\- [ ] NAT Gateway
\- [ ] Load Balancer
\- [ ] unnecessary RDS
\- [ ] large EC2
\- [ ] unnecessary Elastic IP
\- [ ] unnecessary storage
\- [ ] expensive monitoring
\- [ ] paid domain

\### Exit condition

We understand exactly what AWS resources we are about to create and why.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 15 — AWS EC2 DEPLOYMENT ❌

\### Objective

Deploy the Dockerized application to the cloud.

Architecture:

\`\`\`text
Internet
   ↓
EC2
   ↓
Docker
   ↓
FastAPI
   ↓
ML Model
\`\`\`

\### Implement

\- [ ] Launch appropriate EC2 instance
\- [ ] Configure Security Group
\- [ ] SSH
\- [ ] Install required environment
\- [ ] Clone project
\- [ ] Configure environment
\- [ ] Run Docker Compose
\- [ ] Verify containers
\- [ ] Verify API

\### Exit condition

The application is running on EC2.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 16 — NGINX ❌

\### Objective

Learn reverse proxy architecture.

Final flow:

\`\`\`text
Internet
   ↓
Nginx
   ↓
FastAPI
   ↓
ML Pipeline
\`\`\`

\### Implement

\- [ ] Install/configure Nginx
\- [ ] Reverse proxy
\- [ ] Forward traffic to FastAPI
\- [ ] Configure appropriate ports
\- [ ] Test through public IP

\### Exit condition

Users access the API through Nginx rather than directly exposing FastAPI's internal port.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 17 — S3 MODEL BACKUP ❌

\### Objective

Learn basic object storage and model artifact backup.

Architecture:

\`\`\`text
GitHub
   ↓
Source Code

EC2
   ↓
Running Application

S3
   ↓
Model Backup
\`\`\`

\### Implement

\- [ ] Create S3 bucket
\- [ ] Understand bucket/object concepts
\- [ ] Upload model artifact
\- [ ] Verify model exists
\- [ ] Understand appropriate access/security
\- [ ] Keep usage minimal

\### Important

We do **\*\*not\*\*** redesign the entire model-loading system around S3.

The learning objective is:

_>_ **\*\*S3 as model artifact backup/storage.\*\***

\### Exit condition

The trained model is successfully backed up to S3.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 18 — CLOUDWATCH ❌

\### Objective

Learn basic cloud monitoring/logging.

\### Implement

\- [ ] Understand CloudWatch
\- [ ] Basic application logging
\- [ ] Basic EC2 monitoring
\- [ ] View logs/metrics
\- [ ] Verify requests/errors where appropriate

\### Do NOT

Create unnecessarily expensive monitoring infrastructure.

\### Exit condition

We can demonstrate basic monitoring/logging of the deployed application.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 19 — GLOBAL / PUBLIC TESTING ❌

\### Objective

Verify the complete system from outside the local machine.

Test:

\`\`\`text
Public IP
   ↓
Nginx
   ↓
FastAPI
   ↓
Database
   ↓
ML Pipeline
\`\`\`

\### Verify

\- [ ] Public \`/health\`
\- [ ] Public \`/predict\`
\- [ ] Public \`/explain\`
\- [ ] Database logging
\- [ ] Invalid request handling
\- [ ] Docker containers
\- [ ] Nginx
\- [ ] Logs
\- [ ] S3 backup
\- [ ] CloudWatch

\### Exit condition

The entire system works publicly.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 20 — DEMONSTRATION / PORTFOLIO ❌

\### Objective

Capture evidence that the project was successfully completed.

\### Capture

\- [ ] Project architecture
\- [ ] Swagger UI
\- [ ] \`/predict\`
\- [ ] \`/health\`
\- [ ] \`/explain\`
\- [ ] Database prediction record
\- [ ] Docker
\- [ ] Docker Compose
\- [ ] GitHub Actions successful run
\- [ ] EC2
\- [ ] Nginx
\- [ ] S3 model
\- [ ] CloudWatch
\- [ ] Public API
\- [ ] Final end-to-end flow

\### Recording

One complete demonstration:

\`\`\`text
Swagger
  ↓
Prediction
  ↓
Database
  ↓
Explanation
  ↓
Cloud deployment
  ↓
Monitoring
\`\`\`

\### Exit condition

We have enough screenshots/recording to demonstrate the project without needing the AWS deployment to remain online.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# PHASE 21 — AWS CLEANUP / COST SAFETY ❌

\### Objective

End the project safely.

\### After demonstration

\- [ ] Stop/terminate EC2 as appropriate
\- [ ] Remove unnecessary resources
\- [ ] Check S3 resources
\- [ ] Check CloudWatch resources
\- [ ] Check Security Groups
\- [ ] Check billing
\- [ ] Verify no unnecessary resources remain
\- [ ] Confirm project is no longer actively consuming resources

\### Exit condition

Demonstration is complete and unnecessary AWS resources are removed.

**\*\*STATUS: NOT STARTED\*\***

**---**

\# 🔐 THE NON-NEGOTIABLE ORDER

This is the most important part.

From now on, **\*\*we follow this exact sequence\*\***:

\`\`\`text
PHASE 0  Foundations                  ✅
PHASE 1  Project Setup                ✅
PHASE 2  EDA                          ✅
PHASE 3  Data Pipeline                ✅
PHASE 4  Feature Engineering         ✅
PHASE 5  Model Training              ✅
PHASE 6  Evaluation                  ✅
PHASE 7  Model Packaging             ⚠️ SYNC/FIX
PHASE 8  FastAPI                     ⚠️ FINISH
        ↓
PHASE 9  Database + SQLAlchemy ✅
        ↓
PHASE 10 Automated Testing ✅
        ↓
PHASE 11 Docker ✅
        ↓
PHASE 12 Docker Compose ✅
        ↓
PHASE 13 GitHub Actions ✅
        ↓
PHASE 14 AWS Fundamentals + Cost ✅
        ↓
PHASE 15 EC2 ✅
        ↓
PHASE 16 Nginx                        ❌
        ↓
PHASE 17 S3                           ❌
        ↓
PHASE 18 CloudWatch                   ❌
        ↓
PHASE 19 Public Testing               ❌
        ↓
PHASE 20 Demo / Recording             ❌
        ↓
PHASE 21 AWS Cleanup                  ❌
        ↓
             🏁 PROJECT COMPLETE
\`\`\`

\## 🚫 Things we will NOT add

Unless **\*\*you explicitly decide to change the roadmap\*\***, we will **\*\*not\*\*** introduce:

\- ❌ React frontend
\- ❌ Kubernetes
\- ❌ Terraform
\- ❌ Redis
\- ❌ Celery
\- ❌ Kafka
\- ❌ microservices
\- ❌ GPU
\- ❌ model serving platforms
\- ❌ MLflow
\- ❌ complex feature stores
\- ❌ unnecessary model tuning
\- ❌ unnecessary hyperparameter optimization
\- ❌ AWS RDS merely for the sake of it
\- ❌ Load Balancer
\- ❌ NAT Gateway
\- ❌ Route 53/domain
\- ❌ 24/7 deployment
\- ❌ random "production-grade" complexity

Those could all be useful technologies, but **\*\*they are outside this project's learning objective\*\***.

**---**

\# 🧭 OUR ANTI-DRIFT RULE

This is what I want us to use throughout the rest of the project:

\### Rule 1 — One phase at a time

We do **\*\*not\*\*** work on Phase 15 while Phase 10 is incomplete.

\### Rule 2 — Every phase has an exit condition

We don't say:

_> "We kind of did Docker."_

We say:

_> Docker phase is complete because the application successfully builds and runs inside Docker._

\### Rule 3 — No feature creep

If we discover something interesting:

_> "Should we add Redis?"_

We ask:

**\*\*Is Redis required by the locked roadmap?\*\***

If no → **\*\*don't add it.\*\***

\### Rule 4 — Fix before advancing

If something from an earlier phase is broken, we fix it before moving forward.

For example, right now:

**\*\*Pipeline artifact ≠ some API code expectations\*\***

So we fix that first.

\### Rule 5 — Learning comes before implementation

For every major technology:

**\*\*What → Why → Architecture → Implementation → Test → Verify → Next\*\***

Not:

**\*\*Copy code → hope it works → move on.\*\***

\### Rule 6 — AWS comes last

No EC2 before:

\`\`\`text
API
↓
Database
↓
Tests
↓
Docker
↓
Compose
↓
CI
↓
AWS preparation
\`\`\`

\### Rule 7 — Deployment is temporary

The goal is:

\`\`\`text
Build
↓
Deploy
↓
Verify
↓
Record
↓
Shutdown
\`\`\`

Not:

\`\`\`text
Build
↓
Maintain forever
\`\`\`

**---**

\# 📍 OUR EXACT CURRENT POSITION

Right now we are here:

\`\`\`text
Phase 0  ✅
Phase 1  ✅
Phase 2  ✅
Phase 3  ✅
Phase 4  ✅
Phase 5  ✅
Phase 6  ✅
Phase 7  ✅
Phase 8  ✅
Phase 9  ✅
...
Phase 21 ⬜
\`\`\`

\### Therefore, the immediate path is ONLY:

**\*\*1. Fix/synchronize the model packaging/API with the saved pipeline\*\***

**\*\*2. Finish \`/health\`\*\***

**\*\*3. Implement \`/explain\` with SHAP\*\***

**\*\*4. Verify Phase 8 completely\*\***

**\*\*5. Move to Database\*\***

And **\*\*nothing from Docker/AWS should be touched before those steps are completed.\*\***

This roadmap should now be our **\*\*single source of truth\*\***. The original handoff already establishes that the broader Phase 02 must not be declared complete until the API, database, Docker, Compose, GitHub Actions, EC2, public access, and logging requirements are addressed.

**\*\*So yes: before writing any more code, we now have a fixed destination, fixed order, fixed scope, and fixed completion criteria.\*\***
