from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_base import CRUDBase
from app.models import Dish


class CRUDDish(CRUDBase):
    async def view_restaurant_menu(
            self,
            restaurant_id: int,
            session: AsyncSession,
    ):
        menu = await session.execute(
            select(self.model).where(
                self.model.restaurant_id == restaurant_id
            )
        )
        menu = menu.scalars().all()
        if len(menu) == 0:
            raise HTTPException(status_code=404, detail="Меню не найдено")
        return menu


crud_dish = CRUDDish(Dish)
