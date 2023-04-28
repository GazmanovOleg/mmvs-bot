from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b1 = InlineKeyboardButton(text="Service", callback_data='service')
b2 = InlineKeyboardButton(text="About us", callback_data='about_us')
b3 = InlineKeyboardButton(text="Get in touch", callback_data='get_in_touch')

# Создаем объект инлайн-клавиатуры
kb_client : InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[b1],
                     [b2], 
                     [b3]])


bs1 = InlineKeyboardButton(text="Application", callback_data='application')
bs2 = InlineKeyboardButton(text="Software development", callback_data='development')
bs3 = InlineKeyboardButton(text="Video service", callback_data='video_services')
bs4 = InlineKeyboardButton(text="Streaming services", callback_data='broadcasting')
bs5 = InlineKeyboardButton(text="Back", callback_data='back')


kb_service : InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[bs1],
                     [bs2], 
                     [bs3], 
                     [bs4],
                     [bs5]])


bg1 = InlineKeyboardButton(text="appoint a meeting", callback_data='make_appointment')
bg2 = InlineKeyboardButton(text="Back", callback_data='back')
kb_get_in_touch : InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard = [[bg1],[bg2]])


btc = InlineKeyboardButton(text="Back", callback_data='back_to_services')
btc1 = InlineKeyboardButton(text="Оставить заявку", callback_data='make_appointment_with_serv')
kb_back_to_service : InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard = [[btc1],[btc]])


btt = InlineKeyboardButton(text="Back to menu", callback_data='back_to_main_menu')
kb_back_to_time : InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard = [[btt]])

bcon1 = InlineKeyboardButton(text="Zoom", callback_data='con_zoom')
bcon2 = InlineKeyboardButton(text="Telegram", callback_data='con_tg')
bcon_back = InlineKeyboardButton(text="Back", callback_data='con_')


# Создаем объект инлайн-клавиатуры
kb_connect : InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[bcon1],
                     [bcon2], 
                     [bcon_back]])
