from .app import *
from .player_state import AnswearState
from .local_setting import WORDS_API_URL_Street
from .data_fetcher import get_word_from_url
from .keyboards import inline_kb
from .local_setting import WORDS_API_URL_Street, WORDS_API_URL_Home, WORDS_API_URL_Food
from aiogram.dispatcher import FSMContext
import random



@dp.message_handler(commands='street', state="*")
async def street_play(message: types.Message, state: FSMContext):
    """Прои виборі категорії Вулиця, функція отримає іменник з його гендером та зберігає у стані
    AnswearState.street_play_start. Після чого користувачу відображається слово та клавіатура
     з трьома вариантами відповіді"""
    await AnswearState.street_play_start.set()          # Set state
    res = await get_word_from_url(WORDS_API_URL_Street)   # JSON відповідь з бази данних
    async with state.proxy() as data:
        data["step"] = 1
        data["answer"] = res.get("gender")
        data['word'] = res.get("word")
        await message.reply(f"{data['step']}/10.  {data['word']}", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data in ["das", "die", "der"], state=AnswearState.street_play_start)
async def send_random_value(call: types.CallbackQuery, state: FSMContext):
     """"Порівнює відповідь користувача, зі словом з БД, яке надійшло раніше.
     Перевіряє скільки слів відповів користувач. """
     answer = call.data #те що відповів користувач
     async with state.proxy() as data:
         print(data.get("answer"))
         print(f"відповідь {answer}")
         if answer == data.get("answer"):
             res = await get_word_from_url(WORDS_API_URL_Street)
             random_resalt = random.choice(res)
             data["step"] += 1
             data["answer"] = random_resalt.get("gender")
             data["word"] = random_resalt.get("word")
             if data["step"] > 10:
                  await call.message.answer( "The game is over",)
                  await AnswearState.street_play_start.set()
             else:
                  await call.message.answer(
                                       "Richtig  \n" + f"{data['step']}/10.  {data['word']}", reply_markup=inline_kb)

         else:
             await call.message.answer("Leider nein. Versuchen Sie noch mal! \n", reply_markup=inline_kb)





