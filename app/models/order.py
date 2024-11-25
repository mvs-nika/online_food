from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.sql.functions import now

from app.core.db import Base


class OrderStatus(Enum):
    pending = 'pending'
    in_process = 'in_process'
    delivered = 'delivered'
    canceled = 'canceled'


class Order(Base):
    order_data = Column(DateTime, default=now())
    status = Column(SQLEnum(OrderStatus), default=OrderStatus.pending)
    user_id = Column(Integer, ForeignKey('user.id'))
    dish_id = Column(Integer, ForeignKey('dish.id'))
