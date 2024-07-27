from fastapi import FastAPI, Depends, HTTPException, APIRouter, Header
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from .database import SessionLocal, engine
from . import crud, models, schemas, retreatsData
from .settings import settings
import logging


logging.basicConfig(level=logging.INFO)

# Add logging inside your exception handlers or endpoints as needed

app = FastAPI()


# Global Exception Handler for SQLAlchemy errors
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "A database error occurred. Please try again later."},
    )


# Global Exception Handler for Pydantic Validation errors
@app.exception_handler(ValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={"detail": exc.errors()})


# Global Exception Handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a router with the /api/v1/ prefix
api_router = APIRouter(prefix="/api/v1")


def api_key_header(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")


# Create Booking
@api_router.post("/book", response_model=schemas.Booking)
def create_booking(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_header),
):
    try:
        # Check if the user already has a booking for this retreat
        existing_bookings = crud.get_bookings(db, retreat_id=booking.retreat_id)
        for b in existing_bookings:
            if b.user_id == booking.user_id:
                raise HTTPException(
                    status_code=400, detail="Retreat already booked for this user"
                )

        return crud.create_booking(db=db, booking=booking)

    except HTTPException as e:
        raise e
    except Exception as e:
        return {"error": str(e)}


# Get Retreats
@api_router.get("/retreats", response_model=List[schemas.Retreat])
def read_retreats(
    skip: int = 0,
    limit: int = 10,
    filter: Optional[str] = None,
    location: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    api_key: str = Depends(api_key_header),
):
    retreats = crud.get_retreats(
        db, skip=skip, limit=limit, filter=filter, location=location, search=search
    )
    return retreats


@api_router.post("/bulk-insert-retreats")
def bulk_insert_retreats(
    db: Session = Depends(get_db), api_key: str = Depends(api_key_header)
):
    try:
        crud.bulk_insert_retreats(db, retreatsData.retreats)
        return {"message": "Bulk insert completed"}
    except SQLAlchemyError as e:
        # Handle specific database-related errors
        return {"error": "A database error occurred during the bulk insert."}
    except Exception as e:
        # Handle other errors
        return {"error": str(e)}


# Include the router in the app
app.include_router(api_router)
