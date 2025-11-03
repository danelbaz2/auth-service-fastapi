from fastapi import FastAPI
from app.api.routes import auth, health

app = FastAPI(
    title="Auth Service API",
    version="1.0.0",
    description=(
        "Authentication microservice (**FastAPI + SQLAlchemy + Alembic + Postgres**).\n\n"
        "Provides user registration and (soon) login with **JWT**.\n"
        "Uses **Pydantic Settings** for configuration and **Argon2** for password hashing."
    ),
)

TAGS_METADATA = [
    {"name": "Health", "description": "Readiness/liveness"},
    {"name": "POST", "description": "Register, login, and auth flows."},
    ]
app.openapi_tags = TAGS_METADATA

app.include_router(auth.router)
app.include_router(health.router)
