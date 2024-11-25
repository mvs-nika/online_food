from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    describe: Optional[str] = None
    location: str

    class Config:
        orm_mode = True


class RestaurantCreate(RestaurantBase):
    pass

class RestaurantInDB(RestaurantBase):
    id: int

class RestaurantUpdate(BaseModel):
    name: Optional[str]
    describe: Optional[str]
    location: Optional[str]


