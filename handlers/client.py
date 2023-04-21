from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import kb_client, kb_service, kb_get_in_touch
from aiogram.dispatcher.filters import Text
from aiogram_dialog.widgets.kbd import Calendar
from . import texts


'''def _get_datepicker_settings():
    return DatepickerSettings() #some settings

@dp.message_handler(state='*')
async def _main(message: Message):
    datepicker = Datepicker(_get_datepicker_settings())

    markup = datepicker.start_calendar()
    await message.answer('Select a date: ', reply_markup=markup)


@dp.callback_query_handler(Datepicker.datepicker_callback.filter())
async def _process_datepicker(callback_query: CallbackQuery, callback_data: dict):
    datepicker = Datepicker(_get_datepicker_settings())

    date = await datepicker.process(callback_query, callback_data)
    if date:
        await callback_query.message.answer(date.strftime('%d/%m/%Y'))

    await callback_query.answer()'''






async def process_start_command(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, texts.START_TEXT, reply_markup=kb_client)
    except:
        await message.reply("Напишите пожалуйста --> \nhttps://t.me/mmvs_test_bot")





async def main_menu_callback(call: types.CallbackQuery):
    if call.data == "service":
        await call.message.answer(text=texts.SERVICE_TEXT, reply_markup=kb_service)
    if call.data == "about_us":
        await call.message.answer(text=texts.ABOUT_US_TEXT)
    if call.data == "get_in_touch":
        await call.message.answer(text=texts.GET_IN_TOUCH_TEXT, reply_markup=kb_get_in_touch)
    if call.data == "back":
        await call.message.answer(reply_markup=kb_client)
    if call.data == "make_appointment":
        await call.message.answer("fffffffff")
    await bot.answer_callback_query(callback_query_id=call.id)
    
async def service_menu_callback(call: types.CallbackQuery):
    if call.data == "application":
        await call.message.answer(text=texts.APPLICATION_TEXT)
    if call.data == "development":
        await call.message.answer(text=texts.DEVELOPMENT_TEXT)
    if call.data == "video_services":
        await call.message.answer(text=texts.VIDEO_SERVICES)
    if call.data == "broadcasting":
        await call.message.answer(text = texts.BROADCASTING_TEXT)
    if call.data == "back":
        await call.message.answer(reply_markup=kb_client)
    
    await bot.answer_callback_query(callback_query_id=call.id)


 
        



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands = ['start'])
    dp.register_callback_query_handler(main_menu_callback)
    dp.register_callback_query_handler(service_menu_callback)


