from fastapi import FastAPI, APIRouter, Depends
from bson import ObjectId

from .schemas import EventCreate, EventOut
from .database import get_collection
from fastapi import HTTPException
from typing import List

# FastAPI app
app = FastAPI()

# Router prefix → /analytics/…
router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/admin/all", response_model=List[EventOut])
def get_all_events(collection=Depends(get_collection)):
    """Return all analytics events from MongoDB (no auth)."""
    events = list(collection.find())

    if not events:
        raise HTTPException(status_code=404, detail="No events found")

    for event in events:
        event["id"] = str(event["_id"])  # convert ObjectId
        del event["_id"]  # remove _id as it's not in schema

    return events

@router.post("/", response_model=EventOut)  # /analytics/
def record_event(event: EventCreate, collection=Depends(get_collection)):
    """Store a user-generated event in MongoDB."""
    result = collection.insert_one(event.dict())
    event_dict = event.dict()
    event_dict["id"] = str(result.inserted_id)
    return event_dict


@router.get("/health", tags=["internal"])   # /analytics/health
def health():
    return {"status": "ok"}


# Register router with the FastAPI app
app.include_router(router)

