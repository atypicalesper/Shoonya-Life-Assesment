from sqlalchemy.orm import Session
from . import models, schemas

def get_retreats(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Retreat).offset(skip).limit(limit).all()

def create_retreat(db: Session, retreat: schemas.RetreatCreate):
    db_retreat = models.Retreat(**retreat.dict())
    db.add(db_retreat)
    db.commit()
    db.refresh(db_retreat)
    return db_retreat

def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_bookings(db: Session, retreat_id: int):
    return db.query(models.Booking).filter(models.Booking.retreat_id == retreat_id).all()
