from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Content Agent")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "AI Agent Running 🚀"}