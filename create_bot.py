from aiogram import Bot, Dispatcher
from config import TOKEN
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
#storage = MemoryStorage()

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()