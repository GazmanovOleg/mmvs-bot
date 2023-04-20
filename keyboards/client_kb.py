from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/service')
b2 = KeyboardButton('/about_us')
b3 = KeyboardButton('/get_in_touch')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1,b2,b3)

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)

bm1 = KeyboardButton(text="Услуги")
bm2 = KeyboardButton(text="О нас")
bm3 = KeyboardButton(text="Связаться с нами")

kb_main.row(bm1,bm2,bm3)


kb_service = ReplyKeyboardMarkup(resize_keyboard=True)
bs1 = KeyboardButton(text="Приложение")
bs2 = KeyboardButton(text="Разработка")
bs3 = KeyboardButton(text="Видеосервис")
bs4 = KeyboardButton(text="Сервис оналйн вещания")
bs5 = KeyboardButton(text="Back")

kb_service.add(bs1).add(bs2).add(bs3).add(bs4).add(bs5)