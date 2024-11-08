from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from app.core.db import Base

class Review(Base):
    rating = Column(Integer)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
