from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base


class Dish(Base):
    name = Column(String)
    describe = Column(String)
    price = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

