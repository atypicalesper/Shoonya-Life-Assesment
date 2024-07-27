from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Retreat(Base):
    __tablename__ = "retreats"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True)
    price = Column(Float)
    duration = Column(Integer)
    details = Column(String)

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    user_name = Column(String)
    user_email = Column(String)
    user_phone = Column(String)
    retreat_id = Column(Integer, ForeignKey("retreats.id"))
    retreat_title = Column(String)
    retreat_location = Column(String)
    retreat_price = Column(Float)
    retreat_duration = Column(Integer)
    payment_details = Column(String)
    booking_date = Column(Date)
    
    retreat = relationship("Retreat")
