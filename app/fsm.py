from aiogram.fsm.state import StatesGroup, State


class reg(StatesGroup):
    args = State()
    wallet = State()