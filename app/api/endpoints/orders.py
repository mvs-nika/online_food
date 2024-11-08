from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.order import OrderCreate, OrderUpdateStatus
from app.services import order_services

router = APIRouter()

# создание нового заказа.
@router.post('/')
async def create_order(
        order: OrderCreate,
        db: AsyncSession = Depends(get_async_session)):
    return await order_services.create_order(order=order, db=db)

#получение информации о заказе
@router.get('/{order_id}')
async def get_order_by_id(
        order_id: int,
        db: AsyncSession = Depends(get_async_session)):
    return await order_services.get_by_id(order_id=order_id, db=db)

#обновление статуса заказа

@router.put('/{order_id}/status')
async def update_status_order(
        new_status: OrderUpdateStatus,
        order_id: int,
        db: AsyncSession = Depends(get_async_session)):
    return await order_services.update_status(new_status=new_status, order_id=order_id, db=db)

#отмена заказа
@router.delete('/{order_id}/')
async def order_delete(
        order_id: int,
        db: AsyncSession = Depends(get_async_session)):
    return await order_services.delete_by_id(order_id=order_id, db=db)



