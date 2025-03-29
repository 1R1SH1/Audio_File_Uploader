from fastapi import FastAPI
from core.config.settings import Settings
from routes.auth import router as auth_router
from routes.files import router as files_router

settings = Settings()
app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["authentication"])
app.include_router(files_router, prefix="/files", tags=["file management"])

@app.get("/", tags=["health"])
async def health_check():
    return {"status": "ok"}