from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import  Lexicon 
import calendar
from datetime import datetime


def day_by_number(num):
    return ["Пн", "Вт", "Ср", "Чт", "Пт",][num]

def create_date_btn():
    current_datetime = datetime.now()
    day = current_datetime.day
    month = current_datetime.month
    year = current_datetime.year

    tc = calendar.TextCalendar(firstweekday=0)
    date_lst = tc.monthdayscalendar(year,month)

    num_list = [date for week in date_lst for date in week]

    #date_dict = {i:date for week in date_lst for date in week for i in range(len(num_list)) }
    btn_lst = [f"{day_by_number(j)} {i[j]}" for i in date_lst for j in range(len(i)) if i[j] !=0 and j!=5 and j!=6 and i[j]>=day]
    LEXICON = {f"butd_{i+1}":btn_lst[i] for i in range(len(btn_lst))}
    BUTTONS = {f"btnd_{i+1}":str(i+1) for i in range(len(LEXICON))}
    
    return LEXICON, BUTTONS


def create_time_btn():
    LEXICON: dict[str, str] = {
    'buth_1': '13:00',
    'buth_2': '13:30',
    'buth_3': '14:00',
    'buth_4': '14:30',
    'buth_5': '15:00',
    'buth_6': '15:30',
    'buth_7': '16:00',
    'buth_8': '16:30',
    'buth_9': '17:00',
    'buth_10': '17:30',
    'buth_11': '18:00',
    'buth_12': '18:30',
    'buth_13': '19:00',
    'buth_14': '19:30',
    'buth_15': '20:00',}

    BUTTONS: dict[str, str] = {
        'btnh_1': '1',
        'btnh_2': '2',
        'btnh_3': '3',
        'btnh_4': '4',
        'btnh_5': '5',
        'btnh_6': '6',
        'btnh_7': '7',
        'btnh_8': '8',
        'btnh_9': '9',
        'btnh_10': '10',
        'btnh_11': '11',
        'btnh_12': '12',
        'btnh_13': '13',
        'btnh_14': '14',
        'btnh_15': '15',}

    return LEXICON, BUTTONS



def create_inline_kb(width: int, btn_source) -> InlineKeyboardMarkup:
    
    LEXICON, BUTTONS = btn_source()

    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for button in LEXICON:
        buttons.append(InlineKeyboardButton(
                text=LEXICON[button],
                callback_data=button))
    buttons.append(InlineKeyboardButton(
                text="Назад",
                callback_data=list(LEXICON.keys())[0][:5]))
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
    


day_keyboard = create_inline_kb(2,create_date_btn)
hours_keyboard = create_inline_kb(2,create_time_btn)