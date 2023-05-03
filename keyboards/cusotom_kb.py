from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import  Lexicon 
import calendar
from dateutil import relativedelta
from handlers.sqlite import get_busy_times_by_day
from datetime import datetime


def day_by_number(num):
    return ["Mon", "Tue", "Wed", "Thu", "Fri"][num]

def is_holiday():
    return {'January':[1,2,3,4,5,6,7,8],
            'February':[23],
            'March':[8],
            'April':[],
            'May':[1,9],
            'June':[12],
            'July':[],
            'August':[],
            'September':[],
            'Oсtober':[],
            'November':[4],
            'December':[]}

def create_date_btn():
    current_date = datetime.now()
    curr_day = current_date.day
    curr_month = current_date.month
    curr_year = current_date.year
    next_date = (current_date + relativedelta.relativedelta(months=1))
    next_month = next_date.month
    next_year = next_date.year
    tc = calendar.TextCalendar(firstweekday=0)
    date_lst_curr = tc.monthdayscalendar(curr_year,curr_month)
    date_lst_next = tc.monthdayscalendar(next_year,next_month)
    curr_month_name = current_date.strftime('%B')
    next_month_name = next_date.strftime('%B')
    btn_lst_curr = [f"{day_by_number(j)} {i[j]}" for i in date_lst_curr for j in range(len(i)) if i[j] !=0 and j!=5 and j!=6 and i[j]>=curr_day and i[j] not in is_holiday()[curr_month_name]]
    btn_lst_next = [f"{day_by_number(j)} {i[j]}" for i in date_lst_next for j in range(len(i)) if i[j] !=0 and j!=5 and j!=6 and i[j] not in is_holiday()[next_month_name]]
    LEXICON ={curr_month_name:{f"butd1_{i+1}":btn_lst_curr[i] for i in range(len(btn_lst_curr))}},{next_month_name:{f"butd2_{i+1}":btn_lst_next[i] for i in range(len(btn_lst_next))}}
   
    return LEXICON

def create_inline_kb(width: int, LEXICON) -> InlineKeyboardMarkup:
    
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for button in LEXICON:
        buttons.append(InlineKeyboardButton(
                text=LEXICON[button],
                callback_data=button))
    
    '''buttons.append(InlineKeyboardButton(
                text="Назад",
                callback_data=list(LEXICON.keys())[0][:5]))'''
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder

async def create_time_btn(day):
    print(f"Приход")
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

    times = await get_busy_times_by_day(day)
    print(times)
    print(f'бизя таймс {times}')
    date_lst = [i[0] for i in times]
    LEXICON = {i[0]:i[1] for i in LEXICON.items() if i[1] not in date_lst}

    return LEXICON

async def create_inline_kb_time_btn(selected_date):
    kb = create_inline_kb(2,await create_time_btn(selected_date)).row(InlineKeyboardButton(
                text="Back",
                callback_data="buth_"), width=2)
    return  kb.as_markup()

def create_inline_kb_days(atr) -> InlineKeyboardMarkup:
    
    lex1,lex2 = create_date_btn()
    if len(*lex1.values())>0:
       
        curr_keyboard = create_inline_kb(2,*lex1.values())
        if len(*lex1.values())%2!=0:
            curr_keyboard.add(InlineKeyboardButton(text=' ', callback_data="aaa"))
        
        curr_keyboard.row(InlineKeyboardButton(
                        
                        text=str(*lex1.keys()),
                        callback_data='month'), InlineKeyboardButton(
                        text='>>',
                        callback_data='forward'), width=2)
        
    else:
        
        curr_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder().row(InlineKeyboardButton(
                        text=[*lex1.keys()][0],
                        callback_data='month'),InlineKeyboardButton(
                        text='>>',
                        callback_data='forward'), width=2)

    curr_keyboard.row(InlineKeyboardButton(
                text="Back",
                callback_data=f"back_to_main_menu{atr}"), width=2) #проверка если в менсяце не осталось денй
   

    next_keyboard = create_inline_kb(2,*lex2.values())
    if len(*lex2.values())%2!=0:
            next_keyboard.add(InlineKeyboardButton(text=' ', callback_data="aaa"))
    next_keyboard.row(InlineKeyboardButton(
                    text='<<',
                    callback_data='backward'),InlineKeyboardButton(
                        text=[*lex2.keys()][0],
                        callback_data='month'), width=2)
    
    next_keyboard.row(InlineKeyboardButton(
                text="Back",
                callback_data="back_to_main_menu"))
    
    return curr_keyboard.as_markup() ,next_keyboard.as_markup()
    






#day_keyboard = create_inline_kb(2,create_date_btn())


#hours_keyboard = create_inline_kb(2,create_time_btn, day)