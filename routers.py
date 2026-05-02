from collections.abc import Generator

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
import services
from database import SessionLocal

router = APIRouter()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/menus", response_model=list[schemas.MenuResponse], tags=["Menus"])
def get_menus(db: Session = Depends(get_db)):
    return services.get_available_menus(db)


@router.post(
    "/orders",
    response_model=schemas.OrderResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Orders"]
)
def create_order(order_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        return services.place_order(db, order_data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
