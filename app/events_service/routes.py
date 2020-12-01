from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder


from .models import EventModel
from app.events_service.managers.events import Event

router = APIRouter()


@router.get("/events/{event_id}/")
async def get_event(event_id: str):
    event = await Event().get_event(event_id)
    if event:
        return {
            "status_code": 200,
            "data": [event],
            "message": "Event exist"
        }

    return {"status_code": 404, "data": [], "message": "Event not exist"}


@router.get("/events/")
async def get_events():
    events = await Event().get_events()

    return {"status_code": 200, "data": [events], "message": "Events list"}


@router.post("/events/")
async def create_event(event: EventModel):
    transformed_event = jsonable_encoder(event)
    success = await Event(transformed_event).create()
    return {"success": success}


@router.put("/events/{event_id}/")
async def update_event(event_id: str, event: EventModel):
    transformed_event = jsonable_encoder(event)
    transformed_event['id'] = event_id

    success = await Event(transformed_event).update()

    return {"success": success}
