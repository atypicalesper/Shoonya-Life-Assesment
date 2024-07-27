from sqlalchemy.orm import Session
from typing import List
from . import models, schemas


# Seed Retreats
def bulk_insert_retreats(db: Session, retreats_data: List[dict]):
    db.bulk_insert_mappings(models.Retreat, retreats_data)
    db.commit()


def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_retreats(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    filter: str = None,
    location: str = None,
    search: str = None,
) -> List[models.Retreat]:
    query = db.query(models.Retreat)

    if filter:
        query = query.filter(models.Retreat.type.ilike(f"%{filter}%"))

    if location:
        query = query.filter(models.Retreat.location.ilike(f"%{location}%"))

    if search:
        query = query.filter(
            models.Retreat.title.ilike(f"%{search}%")
            | models.Retreat.description.ilike(f"%{search}%")
        )

    return query.offset(skip).limit(limit).all()
