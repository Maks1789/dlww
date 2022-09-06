from aiogram import types
from .app import dp
from .bot_messages import *
from .keyboards import inline_kb_cat
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'], state="*")
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(WelcomeMessage,  reply_markup=inline_kb_cat)


@dp.message_handler(commands=['cancel'], state="*")
async def echo(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(GoodbyMessage)



@dp.callback_query_handler(text="repeat")
async def repeat_messagt(call: types.CallbackQuery):
    await call.message.answer(RepeatMessage,  reply_markup=inline_kb_cat)
