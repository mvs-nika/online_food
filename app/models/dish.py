from sqlalchemy import Column, String, Integer, ForeignKey
from app.core.db import Base


class Dish(Base):
    name = Column(String, nullable=False)
    describe = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    image = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

