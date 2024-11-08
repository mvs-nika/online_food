from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.dish import CreateDish, UpdateDish
from app.services import dish_service

router = APIRouter()


#добавление блюда
@router.post('/{restaurant_id}/menu/')
async def create_dish(
        new_dish: CreateDish,
        db: AsyncSession = Depends(get_async_session)):
    return await dish_service.create_dish(new_dish=new_dish, db=db)


# получение списка меню ресторана
@router.get('/{restaurant_id}/menu/')
async def view_restaurant_menu(
        restaurant_id: int,
        db: AsyncSession = Depends(get_async_session)):
    return await dish_service.view_restaurant_menu(restaurant_id=restaurant_id, db=db)


#обновление информации о блюде
@router.put('/{restaurant_id}/menu/{dish_id}/')
async def update_dish(
        dish_id: int,
        new_dish: UpdateDish,
        db: AsyncSession = Depends(get_async_session)):
    return await dish_service.update_dish(dish_id=dish_id, new_dish=new_dish, db=db)


#удаление блюда из меню

@router.delete('/{restaurant_id}/menu/{dish_id}/')
async def delete_dish(dish_id: int,
                      db: AsyncSession = Depends(get_async_session)):
    return await dish_service.delete_dish(dish_id=dish_id, db=db)
