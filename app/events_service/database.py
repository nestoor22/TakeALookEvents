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


class EventsCollectionOperations:
    def __init__(self):
        self.collection = MongoDBConnection().get_collection('events')

    async def get_event(self, event_id: int) -> dict:
        event = await self.collection.find_one({"id": event_id})
        if event:
            return event

        return {}

    async def add_event(self, event_data: dict) -> bool:
        await self.collection.insert_one(event_data)
        return True

    async def update_event(self, event_data: dict) -> bool:
        event_id = event_data.get('id', '')
        if not event_id:
            return False

        event = await self.collection.find_one({"id": event_id})
        if event:
            new_event = await self.collection.update_one(
                {"id": event_id}, {'$set': event_data})
            if new_event:
                return True
            return False

        return False

    async def delete_event(self, event_id: int) -> bool:
        event = await self.collection.find_one({"id": event_id})
        if event:
            await self.collection.delete_one({"id": event_id})
            return True

        return False
