from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
                                               

from config import TOKEN

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton('/help'))

START_MENU = """
<b>/menu</b> - <em>Главное меню</em>
"""
MAIN_MENU = """
<b>/info</b> - <em>Информация о компании</em>
<b>/services</b> - <em>Информация об услугах</em>
<b>/call_me</b> - <em>Связаться со мной</em>

"""



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=MAIN_MENU, parse_mode="HTML", reply_markup = kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")



@dp.message_handler()
async def echo_message(msg: types.Message):
    if '0' in msg.text:
        await bot.send_message(msg.from_user.id, "YES")
    else:
        await bot.send_message(msg.from_user.id, "NO")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
