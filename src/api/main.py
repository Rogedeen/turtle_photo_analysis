from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import router
import uvicorn

# Kalıcı port yapılandırması
APP_HOST = "127.0.0.1"
APP_PORT = 8080

def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI application.
    Following SOLID principles: Application setup is separated.
    """
    app = FastAPI(
        title="Turtle Photo Analysis API",
        description="API for processing turtle images and identifying species.",
        version="1.0.0"
    )

    # CORS settings to allow requests from React/Vite frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            f"http://localhost:{APP_PORT}",
            f"http://127.0.0.1:{APP_PORT}",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api/v1")
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "src.api.main:app",
        host=APP_HOST,
        port=APP_PORT,
        reload=True,
    )
