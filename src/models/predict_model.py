import pandas as pd
import xgboost as xgb

from src.models.model_loader import load_model


def predict_churn(data: dict):
    """
    Core ML prediction logic.

    Takes raw customer data, passes it through the saved
    preprocessing + XGBoost pipeline, and applies the saved
    prediction threshold.

    Returns:
        prediction: int
        probability: float
    """

    # Convert input data into a single-row DataFrame
    df = pd.DataFrame([data])

    # Load the saved pipeline and threshold.
    # load_model() is cached, so the model is loaded only once.
    pipeline, threshold = load_model()

    # The pipeline handles preprocessing internally.
    proba = pipeline.predict_proba(df)[:, 1][0]

    # Apply the threshold saved during model training.
    prediction = int(proba >= threshold)

    return prediction, float(proba)


def explain_churn(data: dict, top_n: int = 5):
    """
    Generate feature-level Tree SHAP contributions for a
    single customer using XGBoost's native contribution
    calculation.

    The saved sklearn pipeline contains:
        - preprocessing
        - XGBoost model

    The raw customer data is first transformed using the
    exact same preprocessor used during model prediction.

    XGBoost then calculates Tree SHAP contributions using
    pred_contribs=True.

    Returns:
        list of dictionaries containing:
            - feature
            - shap_value
            - impact
    """

    # Convert raw customer data into a single-row DataFrame
    df = pd.DataFrame([data])

    # Load the saved pipeline
    pipeline, _ = load_model()

    # ---------------------------------------------------------
    # Extract pipeline components
    # ---------------------------------------------------------

    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]

    # ---------------------------------------------------------
    # Apply the SAME preprocessing used during prediction
    # ---------------------------------------------------------

    X_transformed = preprocessor.transform(df)

    # XGBoost can work with sparse matrices, but converting to
    # a dense array makes the feature/contribution handling
    # explicit and predictable for this small single-row input.
    if hasattr(X_transformed, "toarray"):
        X_transformed = X_transformed.toarray()

    # ---------------------------------------------------------
    # Get transformed feature names
    # ---------------------------------------------------------

    feature_names = preprocessor.get_feature_names_out()

    # ---------------------------------------------------------
    # Get the underlying XGBoost Booster
    # ---------------------------------------------------------

    booster = model.get_booster()

    # ---------------------------------------------------------
    # Calculate native XGBoost Tree SHAP contributions
    # ---------------------------------------------------------

    dmatrix = xgb.DMatrix(X_transformed)

    contributions = booster.predict(
        dmatrix,
        pred_contribs=True,
    )

    # Single customer → first row
    contributions = contributions[0]

    # XGBoost returns:
    #
    # feature_1 contribution
    # feature_2 contribution
    # ...
    # feature_N contribution
    # bias/base contribution
    #
    # The final value is the bias term, not a feature.
    feature_contributions = contributions[:-1]

    # ---------------------------------------------------------
    # Build explanation records
    # ---------------------------------------------------------

    explanations = []

    for feature_name, shap_value in zip(
        feature_names,
        feature_contributions,
    ):
        shap_value = float(shap_value)

        if shap_value > 0:
            impact = "increases_churn"
        elif shap_value < 0:
            impact = "decreases_churn"
        else:
            impact = "no_effect"

        explanations.append(
            {
                "feature": str(feature_name),
                "shap_value": shap_value,
                "impact": impact,
            }
        )

    # ---------------------------------------------------------
    # Return the most influential features
    # ---------------------------------------------------------

    explanations.sort(
        key=lambda item: abs(item["shap_value"]),
        reverse=True,
    )

    return explanations[:top_n]