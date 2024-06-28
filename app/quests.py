from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from securee import API_TOKEN
import app.qkeyboards as kb


router = Router()
bot = Bot(token=API_TOKEN)


@router.callback_query(F.data == 'q1')
async def q1(callback: CallbackQuery):
    await callback.message.edit_text('Для получения золотых монет:\n1. Подпишитесь на наш новостной канал: https://t.me/MagicalLavka \n2. Нажмите кнопку ниже для проверки подписки.', reply_markup=kb.q1)

