import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
import sqlite3 as sq
import app.keyboards as kb
import app.fsm as fs
import app.func as fun
from securee import API_TOKEN
import asyncio
from datetime import datetime, timedelta

admins = [5643856814, 1976192291]


router = Router()
bot = Bot(token=API_TOKEN)

last_click_times = {}


@router.message(CommandStart())
async def BotStart(message: Message, state: FSMContext, command: CommandObject):
    id = message.from_user.id
    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT user_id FROM users WHERE user_id = {id}')

    if cursor.fetchone() is None:
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (
                       user_id INTEGER,
                       wallet TEXT,
                       balance INTEGER DEFAULT 0,
                       magic TEXT,
                       ref INTEGER,
                       ref_count INTEGER
                       )''')
        conn.commit()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS referal (
                       user_id INTEGER,
                       ref INTEGER
                       )''')
        conn.commit()

        args: int = command.args

        cursor.execute('INSERT INTO referal VALUES (?, ?)', (id, args))
        conn.commit()
        if not args == None:
            cursor.execute(f'SELECT ref_count FROM users WHERE user_id = {int(args)}')
            count = cursor.fetchone()[0]

            cursor.execute('UPDATE users SET ref_count = ? WHERE user_id = ?', (int(count) + 1, args))
            conn.commit()
            conn.close()

            inviter_id = fun.refPay(id, 200)
            await bot.send_message(inviter_id, 'У вас новый ученик, вы получили 200 золотых!', reply_markup=kb.newRef)

        await state.set_state(fs.reg.wallet)
        await message.answer('Введите свой TON кошелёк для определения вашей стихии и магической силы')

        conn.close()
    else:
        await message.answer('Главное меню', reply_markup=kb.main)


@router.callback_query(F.data == 'profile')
async def profile(callback: CallbackQuery):
    id = callback.from_user.id
    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM users WHERE user_id = {id}')
    conn.commit()
    id, wallet, balance, magic, ref, ref_count = cursor.fetchone()
    
    cursor.execute(f'SELECT * FROM inventory WHERE id = {id}')
    inventory = f'Инвентарь:'
    for id, item, count in cursor.fetchall():
        inv = f'\n{item}: {str(count)}'
        inventory = inventory + inv
    if inventory == 'Инвентарь:':
        inventory = 'Ваш инвентарь пуст'

    text = f'Ваш ID: {str(id)}\n\nВаш кошелёк: {wallet}\n\nВаш баланс: {str(balance)} золотых\n\nВаша стихия - {magic}\n\nВаши ученики: {str(ref_count)}\n\n{inventory}'

    await callback.message.edit_text(text, reply_markup=kb.profile)
    conn.commit()
    conn.close()


@router.callback_query(F.data == 'main_menu')
async def main_menu(callback: CallbackQuery):
    await callback.message.edit_text('Главное меню', reply_markup=kb.main)


@router.message(fs.reg.wallet)
async def write_wallet(message: Message, state: FSMContext):
    await state.update_data(wallet = message.text)
    id = message.from_user.id
    
    data = await state.get_data()

    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    mag = fun.randomMagic()

    cursor.execute('INSERT INTO users VALUES (?, ?, 0, ?, 0, 0)', (id, data['wallet'], mag))
    conn.commit()
    conn.close()


    await message.answer(f'Поздравляем ваша стихия - {mag}')

    await message.answer('Главное меню БД', reply_markup=kb.main)
    await state.clear()


@router.callback_query(F.data == 'reff')
async def inviter(callback: CallbackQuery):
    id = callback.from_user.id
    await callback.message.edit_text(f'Ваша реферальная ссылка: https://t.me/MagicalLavkaBot?start={str(id)}', reply_markup=kb.inviter)


@router.callback_query(F.data == 'chest')
async def chest(callback: CallbackQuery):
    await callback.message.edit_text('Этот сундук создан самой богиней Фортуной, испытай свою удачу', reply_markup=kb.chest)


@router.callback_query(F.data == 'open_chest')
async def open_chest(callback: CallbackQuery):
    id = callback.from_user.id

    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT balance FROM users WHERE user_id = {id}')
    bal = cursor.fetchone()[0]
    
    if bal >= 50:
        current_time = datetime.now()
    
        # Проверяем, когда было последнее нажатие
        if id in last_click_times:
            last_click_time = last_click_times[id]
            if current_time - last_click_time < timedelta(seconds=1):
                await bot.answer_callback_query(callback.id, text="Давайте помедленнее", show_alert=True)
                return
    
        # Обновляем время последнего нажатия
        last_click_times[id] = current_time

        try:
            item = fun.randomItem(id)
            await bot.answer_callback_query(callback.id, text=f'Вы получили: {item}', show_alert=True)
        except UnboundLocalError:
            return
            # await bot.answer_callback_query(callback.id, text="Давайте помедленнее", show_alert=True)
        totalBal = bal - 50
        cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (totalBal, id))
        conn.commit()
        conn.close()
    else:
        await bot.answer_callback_query(callback.id, text='Простите, но у вас недостаточно монет', show_alert=True)
    

@router.callback_query(F.data == 'claim')
async def claim(callback: CallbackQuery):
    id = callback.from_user.id

    conn = sq.connect('main_db.db')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM inventory WHERE id = {id}')
    for id, item, count in cursor.fetchall():
        if item == '0.1 ton' and count > 0:
            for admin in admins:
                await bot.send_message(admin, text=f'Пльзователь: {id} заклеймил 0.1 ton х {str(count)}')

            cursor.execute('DELETE FROM inventory WHERE id = ? AND item = ?', (id, '0.1 ton'))
            conn.commit()
            conn.close()


@router.callback_query(F.data == 'seller')
async def seller(callback: CallbackQuery):
    await callback.message.edit_text('Привет, я скупщик предметов. Готов выкупить твои ненужные вещи по <s>почти</s> выгодной цене!', parse_mode='HTML', reply_markup=kb.seller)

