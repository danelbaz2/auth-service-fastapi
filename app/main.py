from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.auth import router
from app.models.user import Base
from app.db import engine

app = FastAPI(title="Auth Service (MVP)")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}
