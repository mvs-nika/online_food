from sqlalchemy import Column, String, Boolean
from app.core.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)#захешированный пароль, в бд всегда храниться захешированный, никогда который ввел пользователь
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)


