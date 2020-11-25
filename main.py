import uvicorn
from server.settings import APP_HOST, APP_PORT

if __name__ == "__main__":
    uvicorn.run("server.app:app", host=APP_HOST, port=APP_PORT, reload=True)
