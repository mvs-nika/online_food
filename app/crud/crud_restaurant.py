from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.crud_base import CRUDBase
from app.models import Restaurant


class CRUDRestaurant(CRUDBase):
    pass


restaurant_crud = CRUDRestaurant(Restaurant)
