from aiogram import types
from .app import dp
from .bot_messages import *
from .keyboards import inline_kb_cat, sens_button, inline_start_cat
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'], state="*")
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(WelcomeMessage,  reply_markup=inline_start_cat)

@dp.callback_query_handler(text="Artikel")
async def art_messagt(call: types.CallbackQuery):
    await call.message.answer("Обери тему\Wähl das Thema 🤖",  reply_markup=inline_kb_cat)


@dp.callback_query_handler(text="Verben")
async def verb_messagt(call: types.CallbackQuery):
    await call.message.answer("Обери правильну відповідь🧙‍♂️",  reply_markup=sens_button)





@dp.message_handler(commands=['cancel'], state="*")
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(GoodbyMessage)



@dp.callback_query_handler(text="repeat")
async def repeat_messagt(call: types.CallbackQuery):
    await call.message.answer(RepeatMessage,  reply_markup=inline_kb_cat)




"Обработка тестов з відповідями"
@dp.message_handler(commands=['sent'])
async def start_sent(message: types.Message):
    await message.reply("У цьому завданні тобі потрібно вибрати правильну форму дієслів", reply_markup=sens_button)


