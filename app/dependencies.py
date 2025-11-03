# app/dependencies.py
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

# One engine for the whole app
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,   # drops dead connections safely
    future=True
)

# Factory for sessions
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    future=True
)

# FastAPI dependency — yields a session per request
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()       # commit successful work
    except Exception:
        db.rollback()     # rollback on error
        raise
    finally:
        db.close()
