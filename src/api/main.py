from fastapi import FastAPI

from src.api.routes.prediction import router as prediction_router

from src.database.database import Base, engine
from src.models.prediction import Prediction


# ---------------------------------------------------------
# Database initialization
# ---------------------------------------------------------

Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------
# FastAPI application
# ---------------------------------------------------------

app = FastAPI(
    title="Customer Churn API",
    version="1.0",
)


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

app.include_router(prediction_router)