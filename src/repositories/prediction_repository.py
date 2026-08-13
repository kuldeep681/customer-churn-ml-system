from sqlalchemy.orm import Session

from src.models.prediction import Prediction


def create_prediction(
    db: Session,
    churn_prediction: int,
    churn_probability: float,
    risk_level: str,
) -> Prediction:
    """
    Create and persist a prediction record.
    """

    prediction = Prediction(
        churn_prediction=churn_prediction,
        churn_probability=churn_probability,
        risk_level=risk_level,
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction