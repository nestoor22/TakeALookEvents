import uvicorn

from app.config import get_config


if __name__ == "__main__":

    config = get_config()

    uvicorn.run(
        app="app.app:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True
    )
