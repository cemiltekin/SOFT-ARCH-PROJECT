from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MenuResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    price: float
    is_available: bool


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=5, max_length=255)
    menu_id: int = Field(gt=0)


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_name: str
    address: str
    menu_id: int
    total_amount: float
    status: str
    created_at: datetime
