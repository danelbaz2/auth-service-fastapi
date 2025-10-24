from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="Auth Service (MVP)")

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.env}
