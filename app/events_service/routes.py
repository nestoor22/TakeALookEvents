from datetime import date, time
from fastapi import APIRouter

from .models import EventModel

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "TEXT"}


@router.get("/events/{event_id}/", response_model=EventModel)
async def get_event(event_id: int):
    return {
        "name": "Movies Night",
        "organizer": {
            "email": "yaroslav.nestor22@gmail.com",
            "first_name": "Yaroslav",
            "last_name": "Nestor"
        },
        "start_date": date.today(),
        "start_time": time(hour=11, minute=40)
    }


@router.post("/events/", response_model=EventModel)
async def create_event(event: EventModel):
    item_dict = event.dict()
    print(item_dict)
    return item_dict