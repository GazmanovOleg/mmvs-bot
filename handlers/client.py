from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_service, kb_get_in_touch, kb_back_to_service, kb_back_to_time
from . import texts
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

ADMIN_LIST = [6206992267]

@dp.message(CommandStart(),StateFilter(default_state))
async def process_start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, texts.START_TEXT, reply_markup=kb_client)
    except:
        await message.reply("Напишите пожалуйста --> \nhttps://t.me/mmvs_test_bot")


@dp.callback_query(Text(text=['service']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    await callback.answer()

@dp.callback_query(Text(text=['about_us']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.ABOUT_US_TEXT, reply_markup=callback.message.reply_markup)
    await callback.answer()

@dp.callback_query(Text(text=['get_in_touch']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    await callback.answer()


@dp.callback_query(Text(text=['application']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.APPLICATION_TEXT, reply_markup=kb_back_to_service)
    await callback.answer()

@dp.callback_query(Text(text=['development']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.DEVELOPMENT_TEXT, reply_markup=kb_back_to_service)
    await callback.answer()
    
@dp.callback_query(Text(text=['video_services']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.VIDEO_SERVICES, reply_markup=kb_back_to_service)
    await callback.answer()


@dp.callback_query(Text(text=['broadcasting']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text = texts.BROADCASTING_TEXT, reply_markup=kb_back_to_service)
    await callback.answer()

@dp.callback_query(Text(text=['back']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.START_TEXT, reply_markup=kb_client)
    await callback.answer()
    
@dp.callback_query(Text(text=['back_to_services']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    await callback.answer()

@dp.callback_query(Text(text=['make_appointment']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext ):
    await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
    
    #await state.set_state(FSMFillForm.fill_date)
    await callback.answer()

@dp.callback_query(Text(startswith=['butd_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'butd_':
        await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    else:
        """Тут будет устанавливаться день"""
        selected_date = create_date_btn()[callback.data]
        meet_id = [i for i in callback.message][4][1].id #meet id is user tg id
        await create_meeting(meeting_id=meet_id) # создание пользователя записи в бд 

        

        #await create_meeting(meeting_id=123456009)
        await edit_meeting(meet_id, 'date', selected_date)
        #await create_meeting(callback.id)
        await state.update_data(date=selected_date) #установка даты
        data = await state.get_data()
        print(f"дата {data['date']}")
        
        await callback.message.edit_text(text="Выберите удобное время:", reply_markup=create_inline_kb(2,create_time_btn(data['date'])))

    await callback.answer()

@dp.callback_query(Text(startswith=['buth_']), StateFilter(default_state))
async def process_forward_press(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'buth_':
        await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
        
    else:
        """Тут будет устанавливаться время"""
        meet_id = [i for i in callback.message][4][1].id
        day = get_meet_by_id(meet_id)[0]
        print(f"день матрен ебён {day}")
        selected_time = create_time_btn(day)[callback.data]
        
        await edit_meeting(meet_id, 'time', selected_time)
        await state.update_data(time=selected_time)
        data = await state.get_data()
        
        answer = (f"Вы записан на {get_meet_by_id(meet_id)}")
        await callback.message.edit_text(text=answer, reply_markup=kb_back_to_time)

    await callback.answer()

@dp.callback_query(Text(text=['back_to_time']))
async def process_forward_press(callback: CallbackQuery):
    meet_id = [i for i in callback.message][4][1].id
    date = get_meet_by_id(meet_id)[0]
    """!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
    await callback.message.edit_text(text="Выберите удобное время:", reply_markup=create_inline_kb(2,create_time_btn(date)))
    await callback.answer()

@dp.message(Command(commands=['sendall']))
async def sendall(message:types.Message):
    
    if message.chat.type == 'private':
        print(message.from_user.id)
        print(ADMIN_LIST)
        if 6206992267 in ADMIN_LIST:  #Написать нормальную проверку по id
            print("приход")
            text = message.text[9:]
            print(f'!!!!!!!!!!!!{get_meetings()}!!!!!!!!1')
            
            #[('Чт 27', '19:30'), ('', ''), ('', ''), ('Ср 26', '')]
            meetings = [ f"{i[0]} {i[1]}" for i in get_meetings()]
            meetings="\n".join(meetings)
            await bot.send_message(message.from_user.id, meetings)
            #await bot.send_message(message.from_user.id, meetings) чтобы отправить админу нужно тупо поменять id на админское  


  
   


