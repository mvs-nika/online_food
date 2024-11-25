from typing import Optional, List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_async_session
from app.core.security import get_current_admin
from app.models import User
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate, RestaurantBase
from app.services import restaurant_service

router = APIRouter()


#Получение списка ресторанов
@router.get('/', response_model=List[RestaurantBase])
async def read_restaurant(
        db: AsyncSession = Depends(get_async_session)):
    restaurants = await restaurant_service.fetch_restaurant(db=db)
    return restaurants


#Получение информации о конкретном ресторане

@router.get('/{restaurant_id}')
async def get_restaurant_by_id(
        restaurant_id: int,
        db: AsyncSession = Depends(get_async_session)):
    restaurant = await restaurant_service.get_restaurant_by_id(db=db, restaurant_id=restaurant_id)
    return restaurant


#Добавление нового ресторана (только для администратора)
@router.post('/')
async def create_restaurant(
        restaurant: RestaurantCreate,
        db: AsyncSession = Depends(get_async_session),
        current_admin: User = Depends(get_current_admin)):
    return await restaurant_service.create_restaurant(restaurant=restaurant, db=db)


#обновление ресторана (только для администратора)
@router.put('/{restaurant_id}')
async def update_restaurant(
        restaurant_id: int,
        restaurant: RestaurantUpdate,
        db: AsyncSession = Depends(get_async_session),
        current_admin: User = Depends(get_current_admin)):
    return await restaurant_service.update_restaurant(restaurant_id=restaurant_id, restaurant=restaurant, db=db)


@router.delete('/{restaurant_id}')
async def delete_restaurant(
        restaurant_id: int,
        db: AsyncSession = Depends(get_async_session),
        current_admin: User = Depends(get_current_admin)):
    return await restaurant_service.delete_restaurant(restaurant_id=restaurant_id, db=db)
