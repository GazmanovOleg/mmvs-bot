from aiogram import types, Dispatcher

from celeryapp import send_email_t
from .texts import what_is_this_text
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_service, kb_get_in_touch, kb_back_to_service, kb_back_to_time, kb_back_to_time, kb_connect
from . import texts
from mail import send_email
import datetime
from .example import Meeting, Meeting_list
from .sqlite import create_meeting, edit_meeting, get_meet_by_id, get_meetings, get_busy_times_by_day
from aiogram.fsm.state import default_state
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from keyboards.cusotom_kb import create_inline_kb, create_date_btn, create_time_btn,  create_inline_kb_days, create_inline_kb_time_btn
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from .FSM import FSMFillForm

router: Router = Router()
ADMIN_LIST = [424726862]

meeting_list = Meeting_list()




@dp.message(CommandStart(),StateFilter(default_state))
async def process_start_command(message: types.Message):
    try:
        user_name = message.from_user.username
        name = message.from_user.full_name
        lg = message.from_user.language_code
        time =  datetime.datetime.now()
        mess = f"username: {user_name}, имя пользователя {name}, язык {lg} \n Время обращения: {time} "
        await create_meeting(meeting_id=message.from_user.id, other = mess)
        await bot.send_message(message.from_user.id, texts.START_TEXT, parse_mode='HTML', reply_markup=kb_client)
    except:
        await message.reply("Напишите")

@dp.callback_query(Text(text=['back_to_main_menu2']),StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """Тут нужна машина состояний"""
    servise = (await state.get_data())['service']
    text = texts.APPLICATION_TEXT
    if servise == 'application':
        text = texts.APPLICATION_TEXT
    if servise == 'development':
        text = texts.DEVELOPMENT_TEXT
    if servise == 'video_services':
        text = texts.VIDEO_SERVICES_TEXT
    if servise == 'broadcasting':
        text = texts.BROADCASTING_TEXT
   
    
    #await edit_meeting(callback.from_user.id, 'service', service_name)
    await callback.message.edit_text(text=text, reply_markup= kb_back_to_service)
    await callback.answer()


@dp.callback_query(Text(text=['make_appointment_with_serv']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext ):
    text_name = [i for i in callback.message][20][1]
    
    service_name = what_is_this_text(text_name)
    meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, service = service_name))
    
    
    await edit_meeting(callback.from_user.id, 'service', service_name)
    await callback.message.edit_text(text="Select a date:", reply_markup= create_inline_kb_days('2')[0])
    await callback.answer()


@dp.callback_query(Text(startswith=['butd']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """callback после нажатия на кнопку дня"""
    if callback.data == 'butd_':
        await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    else:
        num = callback.data[4]
        date = create_date_btn()[0] if num == '1' else create_date_btn()[1]
        month = str(*date.keys())
        date = date[month]
       
       
        """Тут будет устанавливаться день"""

        selected_date = month+" "+date[callback.data]

        meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, date = selected_date))
        #await create_meeting(meeting_id=callback.from_user.id) # создание пользователя записи в бд
        
        await edit_meeting(callback.from_user.id, 'date', selected_date)
        
        await state.update_data(date=selected_date) #установка даты
        await callback.message.edit_text(text="Select a time:", reply_markup=await create_inline_kb_time_btn(selected_date))

    await callback.answer()

@dp.callback_query(Text(startswith=['buth_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """callback после выбора вермени"""
    if callback.data == 'buth_':
              
        await callback.message.edit_text(text='Select a date:', reply_markup=create_inline_kb_days('1')[0])
        
    else:
        """Тут будет устанавливаться время"""
        meet_id = callback.from_user.id
        day = (await get_meet_by_id(meet_id))[0]
        
        selected_time = (await create_time_btn(day))[callback.data]
        
        #selected_time = create_time_btn(day)[callback.data]
        meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, time = selected_time))
        await edit_meeting(callback.from_user.id, 'time', selected_time)
        await state.update_data(time=selected_time)
        text = (f"Choose a convenient means of communication:")
        await callback.message.edit_text(text=text, reply_markup=kb_connect)

    await callback.answer()


@dp.callback_query(Text(startswith=['con_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """callback после выбора конференции"""
    if callback.data == 'con_':
        meet_id = callback.from_user.id
        day = (await get_meet_by_id(meet_id))[0]
        await callback.message.edit_text(text="Select a date:",parse_mode="HTML", reply_markup=await create_inline_kb_time_btn(day))
        
    else:
        """Тут будет устанавливться зум"""
        meet_id = callback.from_user.id

        connect = "tg"
        if callback.data == "con_zoom":
            connect = "zoom"

        meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, connection = connect))
        await edit_meeting(callback.from_user.id, 'connection', connect)
        await state.update_data(connect=connect)
       
        day, time, place = await get_meet_by_id(meet_id)
        answer = (f"The meeting will take place on {day} at {time}. \nOur manager will contact you.")
        
        """Отправка сообщения"""
        user_name = callback.from_user.username
        name = callback.from_user.full_name
        lg = callback.from_user.language_code
        time =  datetime.datetime.now()
        meeting =  await get_meet_by_id(callback.from_user.id)
        day_1, time_1, serv = meeting
        mess = f"username: @{user_name}\nИмя пользователя: {name}\nЯзык {lg}\nВремя обращения: {time}\nВремя записи: {time_1}\nДень записи: {day_1}\nСпособ связи: {serv}"
        
        send_email_t.delay(f'Новая запись:\n{mess}')
        await send_email(f'Новая запись:\n{mess}')
    
        await bot.send_message(424726862, f'Новая запись:\n{mess}')
        await callback.message.edit_text(text=answer, reply_markup=kb_back_to_time)
    await callback.answer()



@dp.callback_query(Text(text=['back_to_time']))
async def process_forward_press(callback: CallbackQuery):
    meet_id = callback.from_user.id
    date = get_meet_by_id(meet_id)[0]
    await callback.message.edit_text(text="Select a time:", reply_markup=create_inline_kb(2,await create_time_btn(date)).as_markup())
    await callback.answer()

@dp.message(Command(commands=['sendall']))
async def sendall(message:types.Message):
    print(message.from_user.id)
    if message.chat.type == 'private':
        if message.from_user.id in ADMIN_LIST: 
        
            meetings = [ f"{i[0]} {i[1]}" for i in (await get_meetings())]
            meetings="\n".join(meetings)
            await bot.send_message(message.from_user.id, meetings)
            #await bot.send_message(message.from_user.id, meetings) чтобы отправить админу нужно тупо поменять id на админское  


  
@dp.callback_query(StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    print(callback.data)
    if callback.data == 'service':
        await callback.message.edit_text(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    if callback.data == 'about_us':
        await callback.message.edit_text(text=texts.ABOUT_US_TEXT, reply_markup=callback.message.reply_markup)
    if callback.data == 'get_in_touch':
        await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    if callback.data == 'application':
        await state.update_data(service ='application')
        await callback.message.edit_text(text=texts.APPLICATION_TEXT, reply_markup=kb_back_to_service, parse_mode="HTML")
    if callback.data == 'development':
        await state.update_data(service ='development')
        await callback.message.edit_text(text=texts.DEVELOPMENT_TEXT, reply_markup=kb_back_to_service)
    if callback.data == 'video_services':
        await state.update_data(service ='video_services')
        await callback.message.edit_text(text=texts.VIDEO_SERVICES_TEXT, reply_markup=kb_back_to_service)
    if callback.data == 'broadcasting':
        await state.update_data(service ='broadcasting')
        await callback.message.edit_text(text = texts.BROADCASTING_TEXT, reply_markup=kb_back_to_service)
    if callback.data == 'back_to_main_menu':
        await callback.message.edit_text(text = texts.START_TEXT, reply_markup=kb_client)
    if callback.data == 'back_to_main_menu1':
        await callback.message.edit_text(text = texts.START_TEXT, reply_markup=kb_client)
    if callback.data == 'back':
        await callback.message.edit_text(text=texts.START_TEXT, reply_markup=kb_client)
    if callback.data == 'back_to_services':
        await callback.message.edit_text(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    if callback.data == 'make_appointment':
        await callback.message.edit_text(text="Select a date:", reply_markup=create_inline_kb_days('1')[0])
    if callback.data == 'asfs':
        await callback.message.edit_text(text="Select a date:", reply_markup=create_inline_kb_days('1')[0])
    if callback.data == 'forward':
         await callback.message.edit_text(text="Select a date:", reply_markup=create_inline_kb_days('1')[1])
    if callback.data == 'backward':
         await callback.message.edit_text(text="Select a date:", reply_markup=create_inline_kb_days('1')[0])
    await callback.answer()

