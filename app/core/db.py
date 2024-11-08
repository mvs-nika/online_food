from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
from app.core.config import settings


class PreBase: #это класс с атрибутами, которые будут во всех таблицах. 1 класс
    @declared_attr #?последовательность действий при использовании атрибута. имя таблицы
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase) #2 класс. базовый класс для всех таблиц, раньше был в database.py
engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True) #чтобы создать ассинхронный движок, нужно указать путь для БД для подключения
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False, expire_on_commit=False)


async def get_async_session(): #создает сессию
    async with AsyncSessionLocal() as async_session:
        yield async_session
