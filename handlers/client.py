from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_service, kb_get_in_touch, kb_back_to_service
from . import texts
from aiogram.filters import Command, CommandStart, Text
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from keyboards.cusotom_kb import day_keyboard, hours_keyboard


router: Router = Router()

@dp.message(CommandStart())
async def process_start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, texts.START_TEXT, reply_markup=kb_client)
    except:
        await message.reply("Напишите пожалуйста --> \nhttps://t.me/mmvs_test_bot")



#await bot.answer_callback_query(callback_query_id=call.id)


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

@dp.callback_query(Text(text=['make_appointment']))
async def process_forward_press(callback: CallbackQuery):
    await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)

    await callback.answer()

@dp.callback_query(Text(startswith=['butd_']))
async def process_forward_press(callback: CallbackQuery):
    if callback.data == 'butd_':
        await callback.message.edit_text(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    else:
        await callback.message.edit_text(text="Выберите удобное время:", reply_markup=hours_keyboard)

    await callback.answer()

@dp.callback_query(Text(startswith=['buth_']))
async def process_forward_press(callback: CallbackQuery):
    if callback.data == 'buth_':
        await callback.message.edit_text(text="Выберите дату:", reply_markup=day_keyboard)
    else:
        await callback.message.edit_text(text="Время выбралось типо там", reply_markup=hours_keyboard)

    await callback.answer()

#def register_handlers_client(dp: Dispatcher):
    
#register_message_handler(process_start_command, commands = ['start'])
  
   


