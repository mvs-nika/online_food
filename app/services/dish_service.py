import base64
import os.path
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.crud.crud_dish import crud_dish
from app.schemas.dish import CreateDish, UpdateDish, DishInDB


async def save_image(image_base64: str) -> str:
    if image_base64.startswith('data:image'):
        image_base64 = image_base64.split(',')[1]

    missing_pading = len(image_base64) % 4
    if missing_pading:
        image_base64 += '=' * (4 - missing_pading)

    try:
        image_data = base64.b64decode(image_base64)
    except base64.binascii.Error:
        raise HTTPException(status_code=400, detail='Некоректное изображение')
    image_name = f'{uuid4}.png'
    image_path = os.path.join(settings.STATIC_IMAGE_PATH, image_name)

    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)

    return image_name


async def create_dish(new_dish: CreateDish, db: AsyncSession):
    image_path = None
    if new_dish.image:
        new_dish.image = await save_image(new_dish.image)

    new_dish = DishInDB(**new_dish.dict()) #**new_dish.dict() почему используем такую конструкцию, потому что пришлось бы присваивать каждому атрибуту значение?
    return await crud_dish.create(obj_in=new_dish, session=db)


async def view_restaurant_menu(restaurant_id: int, db: AsyncSession):
    return await crud_dish.view_restaurant_menu(restaurant_id=restaurant_id, session=db)


async def update_dish(dish_id: int, new_dish: UpdateDish, db=AsyncSession):
    db_dish = await crud_dish.get(obj_id=dish_id, session=db)
    return await crud_dish.update(db_obj=db_dish, obj_in=new_dish, session=db)


async def delete_dish(dish_id: int, db=AsyncSession):
    db_dish = await crud_dish.get(obj_id=dish_id, session=db)
    return await crud_dish.remove(db_obj=db_dish, session=db)
