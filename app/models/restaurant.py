from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.db import Base


class Restaurant(Base):
    name = Column(String, nullable=False)
    describe = Column(String, nullable=True)
    location = Column(String, nullable=True)


