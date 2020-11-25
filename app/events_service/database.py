from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_config

config = get_config()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls
            ).__call__(*args, **kwargs)

        return cls._instances[cls]


class MongoDBConnection(metaclass=Singleton):
    MONGO_DETAILS = f'mongodb://{config.DATABASE_HOST}:{config.DATABASE_PORT}'

    def __init__(self):
        self.client = AsyncIOMotorClient(self.MONGO_DETAILS)
        self.database = self.client.events

    def get_collection(self, collection_name: str):
        return self.database.get_collection(collection_name)
