from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_dish import crud_dish
from app.schemas.dish import CreateDish, UpdateDish


async def create_dish(new_dish: CreateDish, db: AsyncSession):
    return await crud_dish.create(obj_in=new_dish, session=db)


async def view_restaurant_menu(restaurant_id: int, db: AsyncSession):
    return await crud_dish.view_restaurant_menu(restaurant_id=restaurant_id, session=db)


async def update_dish(dish_id: int, new_dish: UpdateDish, db=AsyncSession):
    db_dish = await crud_dish.get(obj_id=dish_id, session=db)
    return await crud_dish.update(db_obj=db_dish, obj_in=new_dish, session=db)


async def delete_dish(dish_id: int, db=AsyncSession):
    db_dish = await crud_dish.get(obj_id=dish_id, session=db)
    return await crud_dish.remove(db_obj=db_dish, session=db)
