from fastapi import APIRouter
from sqlalchemy import text
from app.dependencies import SessionLocal
from app.core.config import settings

router = APIRouter(tags=["Health"])

@router.get(
    "/health",
    summary="API and database health check",
    description=(
        "Checks if the API is running **and** if the database connection works.\n\n"
        "Returns both app and DB status."
    )
)
def health():
    db_status = "ok"
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
    except Exception as e:
        db_status = f"error: {e.__class__.__name__}"

    return {
        "app_status": "ok",
        "db_status": db_status,
        "env": settings.env
    }
