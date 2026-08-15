import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.api.main import app
from src.database.database import Base, get_db


@pytest.fixture
def db_session(tmp_path):
    """
    Create an isolated SQLite database session for each test.
    """

    test_database_path = tmp_path / "test.db"

    test_database_url = f"sqlite:///{test_database_path}"

    test_engine = create_engine(
        test_database_url,
        connect_args={
            "check_same_thread": False,
        },
    )

    TestSessionLocal = sessionmaker(
        bind=test_engine,
        autoflush=False,
        autocommit=False,
    )

    # Create all application tables in the test database.
    Base.metadata.create_all(bind=test_engine)

    db = TestSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=test_engine)
        test_engine.dispose()


@pytest.fixture
def client(db_session):
    """
    Create a FastAPI test client that uses the same
    temporary database session used by the test.
    """

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()