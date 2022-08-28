from aiogram import types
from .app import dp
from .bot_messages import WelcomeMessage
from .keyboards import inline_kb_cat


@dp.message_handler(commands=['start', 'help'])
"""Welcome message + category"""
async def echo(message: types.Message):
    await message.reply(WelcomeMessage,  reply_markup=inline_kb_cat)


