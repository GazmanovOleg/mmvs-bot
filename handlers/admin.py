from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMAdmin(StatesGroup):
    post_title = State()
    post_contet = State()
