from src.api.main import app


def test_api_startup():
    """
    Verify that the FastAPI application can be imported
    and initialized successfully.
    """

    assert app is not None
    assert app.title == "Customer Churn API"
    assert app.version == "1.0"