from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.stream import router as StreamRouter

app = FastAPI(title="StreamMind API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(StreamRouter, prefix="/api/v1")

@app.get("/health")
async def health():
    return {"status": "ok"}
