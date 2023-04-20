from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_main, kb_service
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from . import texts

class Nesting_level:
    def __init__(self):
        self.nesting_level = 0
    def get_nesting_level(self):
        return self.nesting_level
    def nesting_increase(self):
        self.get_nesting_level +=1
    def nestig_level_reduce(self):
        self.nesting_level -=1


'''def get_nesting_level():
    return get_nesting_level'''

async def main_menu_service_command(message: types.Message):
    
    await bot.send_message(message.from_user.id, texts.SERVICE_TEXT , reply_markup=kb_service)

async def main_menu_about_us_command(message: types.Message):
    await bot.send_message(message.from_user.id, texts.ABOUT_US_TEXT)

async def main_menu_get_in_touch(message: types.Message):
    await bot.send_message(message.from_user.id, texts.GET_IN_TOUCH_TEXT)

async def process_start_command(message: types.Message):
    try:
        nestingLevel = 0
        await bot.send_message(message.from_user.id, texts.START_TEXT, reply_markup=kb_client)
    except:
        await message.reply("Напишите пожалуйста --> \nhttps://t.me/mmvs_test_bot")
async def back_command(message: types.Message):
    pass

async def main_menu_kb(message: types.Message):

    await message.answer(text=texts.START_TEXT, reply_markup=kb_main)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, Text(equals='start'))
    dp.register_message_handler(main_menu_service_command, Text(equals='Услуги'))
    dp.register_message_handler(main_menu_about_us_command, Text(equals='О нас'))
    dp.register_message_handler(main_menu_get_in_touch, Text(equals='Связаться с нами'))
   
    dp.register_message_handler(main_menu_kb, Text(equals='/start'))