from fastapi import APIRouter
from app.api.endpoints import auth_router, restaurant_router, order_router, dish_router

main_router = APIRouter() #главный роутер
main_router.include_router(auth_router, tags=['Авторизация'], prefix='/auth') #подключаем к главному ручки с аутентификацией, объединяем по общему тегу и прописываем общий адресс
main_router.include_router(restaurant_router, tags=['Рестораны'], prefix='/restaurants')
main_router.include_router(order_router, tags=['Заказы'], prefix='/orders')
main_router.include_router(dish_router, tags=['Меню'], prefix='/restaurants')

