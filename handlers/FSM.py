from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)


class FSMFillForm(StatesGroup):
    date = State()        # Состояние ожидания ввода имени
    time = State()         # Состояние ожидания ввода возраста
    fill_other = State()      # Состояние ожидания выбора пола

