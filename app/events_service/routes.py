from datetime import date, time
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder


from .models import EventModel
from app.events_service.managers.events import Event

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


@router.post("/events/")
async def create_event(event: EventModel):
    transformed_event = jsonable_encoder(event)
    success = await Event(transformed_event).create()
    return {"success": success}
