from fastapi import FastAPI
from src.api.routes.prediction import router as prediction_router

app = FastAPI(
    title="Customer Churn API",
    version="1.0"
)

app.include_router(prediction_router)