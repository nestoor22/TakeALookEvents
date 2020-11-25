import os
from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.environ.get("APP_HOST")
APP_PORT = os.environ.get("APP_PORT")

DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_PORT = os.environ.get("DATABASE_PORT")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
