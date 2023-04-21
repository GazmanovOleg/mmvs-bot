from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton

kb_client = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text="Услуги", callback_data='service')
b2 = InlineKeyboardButton(text="О нас", callback_data='about_us')
b3 = InlineKeyboardButton(text="Связаться с нами", callback_data='get_in_touch')

kb_client.row(b1,b2,b3)

kb_service = InlineKeyboardMarkup()
bs1 = InlineKeyboardButton(text="Приложение", callback_data='application')
bs2 = InlineKeyboardButton(text="Разработка", callback_data='development')
bs3 = InlineKeyboardButton(text="Видеосервисы", callback_data='video_services')
bs4 = InlineKeyboardButton(text="Сервисы онлайн вещания", callback_data='broadcasting')
bs5 = InlineKeyboardButton(text="Назад", callback_data='back')
kb_service.row(bs1,bs2,bs3,bs4,bs5)

kb_get_in_touch = InlineKeyboardMarkup()
bg1 = InlineKeyboardButton(text="Назначить встерчу", callback_data='make_appointment')
bg2 = InlineKeyboardButton(text="Назад", callback_data='back')
kb_get_in_touch.row(bg1, bg2)
