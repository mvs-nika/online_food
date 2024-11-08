from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_ROOT_PATH: str = ''
    APP_TITLE: str = 'Сервис доставки еды' #Название в свагере, значение по умолчанию, а так подгрузили из .env
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5433/food_delivery'
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    class Config:
        env_file = '.env' #?как подгружается енв файл по этому коду?


settings = Settings()