from abc import ABC, abstractmethod
from typing import List

from app.events_service.email_services.base import BaseEventsEmailService
from app.events_service.email_services.private_event_email_service \
    import PrivateEventEmailService
from app.events_service.email_services.open_event_email_service \
    import OpenEventEmailService


class Event(ABC):
    email_service = BaseEventsEmailService

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

    def send_invatation_to_join(self, resipients_info: List[dict]) -> None:
        self.email_service().send_invatation_to_join(resipients_info)


class OpenEvent(Event):
    email_service = OpenEventEmailService

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class PrivateEvent(Event):
    email_service = PrivateEventEmailService

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
