from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_email = Column(String, unique=True, index=True)
    user_phone = Column(String, comment="Storing country code as well")


class Retreat(Base):
    __tablename__ = "retreats"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(Date, index=True)
    location = Column(String, index=True)
    type = Column(String, index=True)
    condition = Column(String, index=True)
    image = Column(String)
    tag = Column(ARRAY(String))
    price = Column(Float)
    duration = Column(Integer)

    bookings = relationship("Booking", back_populates="retreat")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    retreat_id = Column(Integer, ForeignKey("retreats.id"))
    payment_details = Column(String)
    booking_date = Column(Date, index=True)

    user = relationship("User", back_populates="bookings")
    retreat = relationship("Retreat", back_populates="bookings")
