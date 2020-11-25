import os
from typing import List, Type
from dotenv import load_dotenv

from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    ENV_TYPE: str = "base"
    DEBUG: bool = False
    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = os.getenv("APP_PORT")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")
    DATABASE_PORT: int = os.getenv("DATABASE_PORT")


class DevelopmentConfig(Settings):
    ENV_TYPE: str = "dev"
    DEBUG: bool = True


class TestingConfig(Settings):
    ENV_TYPE: str = "test"
    DEBUG: bool = True


class ProductionConfig(Settings):
    ENV_TYPE: str = "prod"
    APP_HOST: str = os.getenv("PROD_APP_HOST")
    APP_PORT: int = os.getenv("PROD_APP_PORT")
    DATABASE_HOST: str = os.getenv("PROD_DATABASE_HOST")
    DATABASE_NAME: str = os.getenv("PROD_DATABASE_NAME")
    DATABASE_PORT: int = os.getenv("PROD_DATABASE_PORT")


def get_config():
    return config_by_name[os.getenv("ENV_TYPE")]


EXPORT_CONFIGS: List[Type[Settings]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg().ENV_TYPE: cfg() for cfg in EXPORT_CONFIGS}
