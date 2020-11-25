from fastapi import FastAPI

from .events_service.routes import router as events_router


def create_app():
    app = FastAPI(title="TakeALookEvents API")

    app.include_router(events_router)

    return app

app = create_app()
