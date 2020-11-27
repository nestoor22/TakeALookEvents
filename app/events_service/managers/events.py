from abc import ABC, abstractmethod
from typing import List

from ..database import EventsCollectionOperations


class Event(ABC):
    db_collection = EventsCollectionOperations

    def __init__(self, info: dict):
        self.event_info = info

    @abstractmethod
    def create(self):
        raise NotImplemented()

    @abstractmethod
    def update(self):
        raise NotImplemented()

    @abstractmethod
    def delete(self):
        raise NotImplemented()

    def get_events_participants(self) -> List[str]:
        return self.event_info['participants']

    def set_events_participants(self, participants: List[str]) -> List[str]:
        self.event_info['participants'] = participants
        return self.event_info['participants']


class OpenEvent(Event):

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class PrivateEvent(Event):

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
