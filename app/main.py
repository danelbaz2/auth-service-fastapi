from fastapi import FastAPI

app = FastAPI(title="Auth Service (MVP)")

@app.get("/health")
def health():
    return {"status": "ok"}
