from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)



main_profile = InlineKeyboardButton(text='ПРОФИЛЬ', callback_data='profile')

main_invite = InlineKeyboardButton(text='ПРИГЛАСИТЬ ДРУГА', callback_data='reff')

main_chest = InlineKeyboardButton(text='СУНДУК', callback_data='chest')

main_claim = InlineKeyboardButton(text='КЛЕЙМ НАГРАД', callback_data='claim')

main_seller = InlineKeyboardButton(text='СКУПЩИК', callback_data='seller')

main = InlineKeyboardMarkup(inline_keyboard=[[main_profile, main_chest], [main_seller, main_claim], [main_invite]])


profile_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

profile = InlineKeyboardMarkup(inline_keyboard=[[profile_cancel]])


inviter_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

inviter = InlineKeyboardMarkup(inline_keyboard=[[inviter_cancel]])


newRef_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

newRef = InlineKeyboardMarkup(inline_keyboard=[[newRef_cancel]])


chest_open = InlineKeyboardButton(text='ОТКРЫТЬ СУНДУК (50 золотых)', callback_data='open_chest')

chest_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

chest = InlineKeyboardMarkup(inline_keyboard=[[chest_open], [chest_cancel]])