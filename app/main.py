from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, init_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=list[schemas.Retreat])
def hello(db: Session = Depends(get_db)):
    return "Hello Shoonya Life"


# crud.py
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models


def get_retreats(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    filter: Optional[str] = None,
    location: Optional[str] = None,
    search: Optional[str] = None,
) -> List[models.Retreat]:
    query = db.query(models.Retreat)

    if filter:
        query = query.filter(models.Retreat.category.ilike(f"%{filter}%"))

    if location:
        query = query.filter(models.Retreat.location.ilike(f"%{location}%"))

    if search:
        query = query.filter(
            models.Retreat.title.ilike(f"%{search}%")
            | models.Retreat.description.ilike(f"%{search}%")
        )

    return query.offset(skip).limit(limit).all()


# Create Booking
@app.post("/book", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    # Check if the user already has a booking for this retreat
    existing_bookings = crud.get_bookings(db, retreat_id=booking.retreat_id)
    for b in existing_bookings:
        if b.user_id == booking.user_id:
            raise HTTPException(
                status_code=400, detail="Retreat already booked for this user"
            )

    return crud.create_booking(db=db, booking=booking)
