import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from securee import API_TOKEN
import sqlite3 as sq

from app.handlers import router
# import logging

bot = Bot(token=API_TOKEN)
dp = Dispatcher()




# s




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())