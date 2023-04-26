from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b1 = InlineKeyboardButton(text="Услуги", callback_data='service')
b2 = InlineKeyboardButton(text="О нас", callback_data='about_us')
b3 = InlineKeyboardButton(text="Связаться с нами", callback_data='get_in_touch')

# Создаем объект инлайн-клавиатуры
kb_client : InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[b1],
                     [b2], 
                     [b3]])


bs1 = InlineKeyboardButton(text="Приложение", callback_data='application')
bs2 = InlineKeyboardButton(text="Разработка", callback_data='development')
bs3 = InlineKeyboardButton(text="Видеосервисы", callback_data='video_services')
bs4 = InlineKeyboardButton(text="Сервисы онлайн вещания", callback_data='broadcasting')
bs5 = InlineKeyboardButton(text="Назад", callback_data='back')


kb_service : InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[bs1],
                     [bs2], 
                     [bs3], 
                     [bs4],
                     [bs5]])




bg1 = InlineKeyboardButton(text="Назначить встерчу", callback_data='make_appointment')
bg2 = InlineKeyboardButton(text="Назад", callback_data='back')
kb_get_in_touch : InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard = [[bg1],[bg2]])


btc = InlineKeyboardButton(text="Назад", callback_data='back_to_services')
kb_back_to_service : InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard = [[btc]])


btt = InlineKeyboardButton(text="Назад", callback_data='back_to_time')
kb_back_to_time : InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard = [[btt]])