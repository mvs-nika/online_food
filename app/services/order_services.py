from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.crud_order import crud_order
from app.schemas.order import OrderCreate, OrderUpdateStatus


async def create_order(order: OrderCreate, db: AsyncSession):
    return await crud_order.create(obj_in=order, session=db)


async def get_by_id(order_id: int, db: AsyncSession):
    return await crud_order.get(obj_id=order_id, session=db)


async def update_status(new_status: OrderUpdateStatus, order_id: int, db: AsyncSession):
    db_order = await crud_order.get(obj_id=order_id, session=db)
    return await crud_order.update(db_obj=db_order, obj_in=new_status, session=db)


async def delete_by_id(order_id:int, db:AsyncSession):
    db_order = await crud_order.get(obj_id=order_id, session=db)
    return await crud_order.remove(db_obj=db_order, session=db)
