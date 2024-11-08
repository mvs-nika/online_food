from typing import Optional

from pydantic import BaseModel


class DishBase(BaseModel):
    name: str
    describe: str
    price: int
    restaurant_id: int


class CreateDish(DishBase):
    pass


class UpdateDish(BaseModel):
    name: Optional[str]
    describe: Optional[str]
    price: Optional[int]
    restaurant_id: Optional[int]

