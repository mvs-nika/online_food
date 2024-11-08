from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.db import Base


class Restaurant(Base):
    name = Column(String)
    describe = Column(String)
    location = Column(String)


