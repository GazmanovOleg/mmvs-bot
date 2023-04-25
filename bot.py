from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from create_bot import dp, bot                                      
from handlers import client, admin, other
import asyncio
from aiogram import Router
from handlers.sqlite import db_start

async def on_startup():
    print("Бот вышел в онлайн")

#client.register_handlers_client(dp)
#other.register_handlers_other(dp)

router = Router()

async def main():
    dp.include_router(router)
    await on_startup()
    await db_start()
    await dp.start_polling(bot, on_startup=on_startup)
    

if __name__ == '__main__':
   
    asyncio.run(main())
    #dp.run_polling(bot)
    







