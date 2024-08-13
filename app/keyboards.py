from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)



main_profile = InlineKeyboardButton(text='ПРОФИЛЬ', callback_data='profile')

main_invite = InlineKeyboardButton(text='ПРИГЛАСИТЬ ДРУГА', callback_data='reff')

main_chest = InlineKeyboardButton(text='СУНДУК', callback_data='chest')

main_claim = InlineKeyboardButton(text='КЛЕЙМ', callback_data='claim')

main_gildia = InlineKeyboardButton(text='ГИЛЬДИЯ', callback_data='gildia')

main_top = InlineKeyboardButton(text='ТОП', callback_data='top')

main = InlineKeyboardMarkup(inline_keyboard=[[main_profile, main_chest], [main_claim, main_gildia, main_top], [main_invite]])


profile_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

profile = InlineKeyboardMarkup(inline_keyboard=[[profile_cancel]])


inviter_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

inviter = InlineKeyboardMarkup(inline_keyboard=[[inviter_cancel]])


newRef_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

newRef = InlineKeyboardMarkup(inline_keyboard=[[newRef_cancel]])


chest_open = InlineKeyboardButton(text='ОТКРЫТЬ СУНДУК (50 золотых)', callback_data='open_chest')

chest_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

chest = InlineKeyboardMarkup(inline_keyboard=[[chest_open], [chest_cancel]])


seller_sell = InlineKeyboardButton(text='ПРОДАТЬ ПРЕДМЕТЫ', callback_data='sell')

seller_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='gildia')

seller = InlineKeyboardMarkup(inline_keyboard=[[seller_sell], [seller_cancel]])


gildia_seller = InlineKeyboardButton(text='СКУПЩИК', callback_data='seller')

gildia_quests = InlineKeyboardButton(text='КВЕСТЫ', callback_data='quests')

gildia_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='main_menu')

gildia = InlineKeyboardMarkup(inline_keyboard=[[gildia_seller, gildia_quests], [gildia_cancel]])


quests_cancel = InlineKeyboardButton(text='НАЗАД', callback_data='gildia')

quests_q1 = InlineKeyboardButton(text='Magic Lavka', callback_data='q1')

quests = InlineKeyboardMarkup(inline_keyboard=[[quests_q1], [quests_cancel]])