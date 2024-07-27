from pydantic import BaseModel
from typing import Optional

class RetreatBase(BaseModel):
    title: str
    location: str
    price: float
    duration: int
    details: Optional[str] = None

class RetreatCreate(RetreatBase):
    pass

class Retreat(RetreatBase):
    id: int

    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    user_phone: str
    retreat_id: int
    retreat_title: str
    retreat_location: str
    retreat_price: float
    retreat_duration: int
    payment_details: str
    booking_date: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True
