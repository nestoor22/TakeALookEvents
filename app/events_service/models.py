from datetime import date, time
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)


class EventModel(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(min_length=100, max_length=1000)
    event_type: Optional[str] = Field(default='open')

    organizer: UserModel = None

    participants: List[UserModel] = []
    min_participants: int = Field(default=1)
    max_participants: int = Field(default=1)

    place: str = Field(...)

    start_date: date = Field(...)
    start_time: time = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Movies Night",
                "organizer": {
                    "email": "test@test.com",
                    "first_name": "Yaroslav",
                    "last_name": "Nestor"
                },
                "min_participants": 10,
                "max_participants": 22,
                "place": "Lviv, Ukraine",
                "start_date": date.today(),
                "start_time": time(hour=11, minute=40)
            }
        }