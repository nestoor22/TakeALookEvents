from uuid import uuid4
from typing import List

from ..database import EventsCollectionOperations


class Event:
    db_collection = EventsCollectionOperations

    def __init__(self, info: dict):
        self.event_info = info

    async def create(self):
        self.event_info['_id'] = uuid4()
        return await self.db_collection().add_event(self.event_info)

    async def update(self):
        return await self.db_collection().update_event(self.event_info)

    async def delete(self, event_id: str) -> bool:
        return await self.db_collection().delete_event(event_id)

    def get_events_participants(self) -> List[str]:
        return self.event_info['participants']

    def set_events_participants(self, participants: List[str]) -> List[str]:
        self.event_info['participants'] = participants
        return self.event_info['participants']
