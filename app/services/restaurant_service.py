from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import restaurant_crud
from app.models import Restaurant
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate


async def fetch_restaurant(db: AsyncSession):
    restaurants = await restaurant_crud.get_multi(session=db)
    return restaurants


async def get_restaurant_by_id(db: AsyncSession, restaurant_id: int):
    restaurant = await restaurant_crud.get(session=db, obj_id=restaurant_id)
    return restaurant

async def create_restaurant(restaurant: RestaurantCreate, db: AsyncSession):
    return await restaurant_crud.create(obj_in=restaurant, session=db)

async def update_restaurant(restaurant_id: int, restaurant = RestaurantUpdate, db = AsyncSession):
    db_restaurant = await restaurant_crud.get(obj_id=restaurant_id, session=db)
    return await restaurant_crud.update(db_obj=db_restaurant, obj_in=restaurant, session=db)

async def delete_restaurant(db: AsyncSession, restaurant_id: int):
    restaurant = await restaurant_crud.get(session=db, obj_id=restaurant_id)
    return await restaurant_crud.remove(db_obj=restaurant, session=db)


