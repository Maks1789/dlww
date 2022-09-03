from aiogram import types
from .app import dp
from .bot_messages import *
from .keyboards import inline_kb_cat
from .player_state import AnswearState


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply(WelcomeMessage,  reply_markup=inline_kb_cat)


@dp.callback_query_handler(text="repeat")
async def repeat_messagt(call: types.CallbackQuery):
    await call.message.answer(RepeatMessage,  reply_markup=inline_kb_cat)
