from aiogram import types, Dispatcher
from .texts import what_is_this_text
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_service, kb_get_in_touch, kb_back_to_service, kb_back_to_time, kb_back_to_time, kb_connect
from . import texts
from .example import Meeting, Meeting_list
from .sqlite import create_meeting, edit_meeting, get_meet_by_id, get_meetings, get_busy_times_by_day
from aiogram.fsm.state import default_state
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from keyboards.cusotom_kb import day_keyboard, create_inline_kb, create_date_btn, create_time_btn
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
        await bot.send_message(message.from_user.id, texts.START_TEXT, parse_mode='HTML', reply_markup=kb_client)
    except:
        await message.reply("Напишите пожалуйста --> \nhttps://t.me/mmvs_test_bot")



@dp.callback_query(Text(text=['make_appointment_with_serv']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext ):
    text_name = [i for i in callback.message][20][1]
    service_name = what_is_this_text(text_name)
    meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, service = service_name))
    
    await create_meeting(meeting_id=callback.from_user.id)
    
    await edit_meeting(callback.from_user.id, 'service', service_name)
    await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
    await callback.answer()


@dp.callback_query(Text(startswith=['butd_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """callback после нажатия на кнопку дня"""
    if callback.data == 'butd_':
        await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    else:
        """Тут будет устанавливаться день"""
        
        selected_date = create_date_btn()[callback.data]

        meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, date = selected_date))
        await create_meeting(meeting_id=callback.from_user.id) # создание пользователя записи в бд
        print(f"ебана рама {type(selected_date)}")
        await edit_meeting(callback.from_user.id, 'date', selected_date)
        
        await state.update_data(date=selected_date) #установка даты
        await callback.message.edit_text(text="Выберите удобное время:", reply_markup=create_inline_kb(2,await create_time_btn(selected_date)))

    await callback.answer()

@dp.callback_query(Text(startswith=['buth_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """callback после выбора вермени"""
    if callback.data == 'buth_':
        await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
        
    else:
        """Тут будет устанавливаться время"""
        meet_id = callback.from_user.id
        day = get_meet_by_id(meet_id)[0]
        selected_time = await create_time_btn(day)[callback.data]
        meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, time = selected_time))
        await edit_meeting(callback.from_user.id, 'time', selected_time)
        await state.update_data(time=selected_time)
        text = (f"Выбреите удобное средство связи")
        await callback.message.edit_text(text=text, reply_markup=kb_connect)

    await callback.answer()


@dp.callback_query(Text(startswith=['con_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    """callback после выбора конференции"""
    if callback.data == 'con_':
        await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
        
    else:
        """Тут будет устанавливться зум"""
        meet_id = callback.from_user.id
        print(f"!!!!!!{callback.data}!!!!!")
        connect = "tg"
        if callback.data == "con_zoom":
            connect = "zoom"

        meeting_list.add_to_list(Meeting(meeting_id = callback.from_user.id, connection = connect))
        await edit_meeting(callback.from_user.id, 'connection', connect)
        await state.update_data(connect=connect)
        day, time = get_meet_by_id(meet_id)
        answer = (f"Вы записаны на {day} в {time}. \n Наш менеджер свяжется с вами.")
        
        await bot.send_message(424726862, f'ewfewrw{get_meet_by_id(callback.from_user.id)}')
        await callback.message.edit_text(text=answer, reply_markup=kb_back_to_time)
    await callback.answer()



@dp.callback_query(Text(text=['back_to_time']))
async def process_forward_press(callback: CallbackQuery):
    meet_id = callback.from_user.id
    date = get_meet_by_id(meet_id)[0]
    await callback.message.edit_text(text="Выберите удобное время:", reply_markup=create_inline_kb(2,await create_time_btn(date)))
    await callback.answer()

@dp.message(Command(commands=['sendall']))
async def sendall(message:types.Message):
    print(message.from_user.id)
    if message.chat.type == 'private':
        if message.from_user.id in ADMIN_LIST: 
            print(get_meetings())
            meetings = [ f"{i[0]} {i[1]}" for i in get_meetings()]
            meetings="\n".join(meetings)
            await bot.send_message(message.from_user.id, meetings)
            #await bot.send_message(message.from_user.id, meetings) чтобы отправить админу нужно тупо поменять id на админское  


  
@dp.callback_query()
async def process_forward_press(callback: CallbackQuery):
    if callback.data == 'service':
        await callback.message.edit_text(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    if callback.data == 'about_us':
        await callback.message.edit_text(text=texts.ABOUT_US_TEXT, reply_markup=callback.message.reply_markup)
    if callback.data == 'get_in_touch':
        await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    if callback.data == 'application':
        await callback.message.edit_text(text=texts.APPLICATION_TEXT, reply_markup=kb_back_to_service, parse_mode="HTML")
    if callback.data == 'development':
        await callback.message.edit_text(text=texts.DEVELOPMENT_TEXT, reply_markup=kb_back_to_service)
    if callback.data == 'video_services':
        await callback.message.edit_text(text=texts.VIDEO_SERVICES, reply_markup=kb_back_to_service)
    if callback.data == 'broadcasting':
        await callback.message.edit_text(text = texts.BROADCASTING_TEXT, reply_markup=kb_back_to_service)
    if callback.data == 'back_to_main_menu':
        await callback.message.edit_text(text = texts.START_TEXT, reply_markup=kb_client)
    if callback.data == 'back':
        await callback.message.edit_text(text=texts.START_TEXT, reply_markup=kb_client)
    if callback.data == 'back_to_services':
        await callback.message.edit_text(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    if callback.data == 'make_appointment':
        await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
    if callback.data == 'asfs':
        await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
    await callback.answer()

