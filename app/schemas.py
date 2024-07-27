from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


# User Schemas
class UserBase(BaseModel):

    user_name: str
    user_email: str
    user_phone: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Retreat Schemas
class RetreatBase(BaseModel):
    title: str
    description: Optional[str] = None
    date: date
    location: str
    type: str
    condition: str
    image: Optional[str] = None
    tag: Optional[List[str]] = None
    price: float = Field(..., gt=0)  # Ensure price is greater than 0
    duration: int = Field(..., gt=0)  # Ensure duration is greater than 0


class RetreatCreate(RetreatBase):
    pass


class Retreat(RetreatBase):
    id: int

    class Config:
        orm_mode = True


# Booking Schemas
class BookingBase(BaseModel):
    user_id: int
    retreat_id: int
    payment_details: str
    booking_date: date


class BookingCreate(BookingBase):
    pass


class Booking(BookingBase):
    id: int
    user: Optional[User] = None
    retreat: Optional[Retreat] = None

    class Config:
        orm_mode = True
