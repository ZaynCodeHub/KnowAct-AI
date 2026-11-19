
from fastapi import FastAPI

app = FastAPI(
    title="KnowAct AI API",
    version="0.1.0",
)

@app.get("/health/live")
def health_live():
    return {
        "status": "ok",
        "service": "knowact-api",
    }
