from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)


q1_check = InlineKeyboardButton(text='Проверить подписку', callback_data='q1_check')

q1_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='quests')

q1 = InlineKeyboardMarkup(inline_keyboard=[[q1_check], [q1_cancel]])