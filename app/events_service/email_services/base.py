from abc import ABC, abstractmethod


class BaseEventsEmailService(ABC):

    @staticmethod
    @abstractmethod
    def send_invatation_to_join(recepient_info):
        raise NotImplemented()
