from src.models.prediction import Prediction


def get_valid_payload():
    """
    Return a valid customer payload used by prediction tests.
    """

    return {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 60,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "Yes",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Two year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Credit card (automatic)",
        "MonthlyCharges": 50.00,
        "TotalCharges": 3000.00,
    }


# ============================================================
# /predict
# ============================================================

def test_predict_valid_request(client):
    """
    Verify that a valid customer request returns
    a successful churn prediction.
    """

    payload = get_valid_payload()

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 200

    result = response.json()

    assert "churn_prediction" in result
    assert "churn_probability" in result
    assert "risk_level" in result

    assert result["churn_prediction"] in [0, 1]
    assert 0.0 <= result["churn_probability"] <= 1.0
    assert result["risk_level"] in ["Low", "Medium", "High"]


def test_predict_missing_field(client):
    """
    Verify that a request with a missing required field
    is rejected by the API.
    """

    payload = get_valid_payload()

    del payload["tenure"]

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 422


def test_predict_invalid_categorical_value(client):
    """
    Verify that an invalid categorical value is rejected.
    """

    payload = get_valid_payload()

    payload["gender"] = "Unknown"

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 422


def test_predict_invalid_numeric_value(client):
    """
    Verify that an invalid numeric value is rejected.
    """

    payload = get_valid_payload()

    payload["SeniorCitizen"] = 5

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 422


# ============================================================
# Database logging
# ============================================================

def test_prediction_is_saved_to_database(client, db_session):
    """
    Verify that a successful /predict request
    creates a prediction record in the database.
    """

    payload = get_valid_payload()

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 200

    result = response.json()

    records = db_session.query(Prediction).all()

    assert len(records) == 1

    record = records[0]

    assert record.churn_prediction == result["churn_prediction"]
    assert record.churn_probability == result["churn_probability"]
    assert record.risk_level == result["risk_level"]
    assert record.created_at is not None


# ============================================================
# /explain
# ============================================================

def test_explain_valid_request(client):
    """
    Verify that a valid /explain request returns
    prediction and SHAP explanation data.
    """

    payload = get_valid_payload()

    response = client.post(
        "/explain",
        json=payload,
    )

    assert response.status_code == 200

    result = response.json()

    assert "churn_prediction" in result
    assert "churn_probability" in result
    assert "risk_level" in result
    assert "explanation" in result

    assert result["churn_prediction"] in [0, 1]
    assert 0.0 <= result["churn_probability"] <= 1.0
    assert result["risk_level"] in ["Low", "Medium", "High"]

    assert isinstance(result["explanation"], list)


def test_explain_contains_shap_features(client):
    """
    Verify that the /explain endpoint returns
    structured SHAP feature explanations.
    """

    payload = get_valid_payload()

    response = client.post(
        "/explain",
        json=payload,
    )

    assert response.status_code == 200

    result = response.json()

    explanation = result["explanation"]

    assert len(explanation) > 0

    for item in explanation:
        assert "feature" in item
        assert "shap_value" in item
        assert "impact" in item

        assert isinstance(item["feature"], str)
        assert isinstance(item["shap_value"], (int, float))
        assert item["impact"] in [
            "increases_churn",
            "decreases_churn",
        ]


def test_explain_does_not_save_prediction(client, db_session):
    """
    Verify that /explain generates an explanation
    but does not create a prediction database record.
    """

    payload = get_valid_payload()

    response = client.post(
        "/explain",
        json=payload,
    )

    assert response.status_code == 200

    records = db_session.query(Prediction).all()

    assert len(records) == 0


# ============================================================
# /explain validation
# ============================================================

def test_explain_invalid_request(client):
    """
    Verify that invalid input is rejected by /explain.
    """

    payload = get_valid_payload()

    payload["gender"] = "Unknown"

    response = client.post(
        "/explain",
        json=payload,
    )

    assert response.status_code == 422