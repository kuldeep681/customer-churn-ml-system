from pathlib import Path
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config.config_loader import load_config


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

config = load_config()

database_url = os.getenv(
    "DATABASE_URL",
    config["database"]["url"],
)


# ---------------------------------------------------------
# SQLite database path
# ---------------------------------------------------------

if database_url.startswith("sqlite:///"):
    relative_path = database_url.replace("sqlite:///", "", 1)

    base_path = Path(__file__).resolve().parents[2]
    database_path = base_path / relative_path

    database_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    database_url = f"sqlite:///{database_path}"


# ---------------------------------------------------------
# Database Engine
# ---------------------------------------------------------

if database_url.startswith("sqlite"):
    engine = create_engine(
        database_url,
        connect_args={
            "check_same_thread": False,
        },
    )
else:
    engine = create_engine(database_url)


# ---------------------------------------------------------
# Session Factory
# ---------------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# ---------------------------------------------------------
# Declarative Base
# ---------------------------------------------------------

class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------
# Database Dependency
# ---------------------------------------------------------

def get_db():
    """
    Provide a database session for a single request.

    The session is always closed after the request finishes.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()