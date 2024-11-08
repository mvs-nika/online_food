from datetime import datetime

from pydantic import BaseModel, Field


class OrderBase(BaseModel):
    status: str
    user_id: int
    restaurant_id: int


class OrderCreate(OrderBase):
    pass


class OrderInDB(OrderBase):
    order_data: datetime


class OrderUpdateStatus(BaseModel):
    status: str

