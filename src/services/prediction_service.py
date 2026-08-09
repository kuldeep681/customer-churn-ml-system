from src.models.predict_model import predict_churn


def predict(data: dict):
    """
    Service layer:
    - Calls model
    - Formats response
    """

    prediction, probability = predict_churn(data)

    return {
        "churn_prediction": prediction,
        "churn_probability": probability
    }