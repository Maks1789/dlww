import random
from aiogram.dispatcher import FSMContext
from .app import *
from .data_fetcher import get_word_from_url
from .keyboards import inline_kb, reapeat_button
from .local_setting import WORDS_API_URL_Street, WORDS_API_URL_Home, WORDS_API_URL_Food
from .player_state import AnswearState
from .bot_messages import RichtigMessage, FalschMessage


def category_word(data):
    """result_call - Зберігає категорію, яку обрав користувач """
    global result_call
    if data == "street":
        result_call = WORDS_API_URL_Street
    elif data == "home":
        result_call = WORDS_API_URL_Home
    elif data == "food":
        result_call = WORDS_API_URL_Food
    return result_call


@dp.callback_query_handler(lambda c: c.data in ["street", "home", "food"], state="*")
async def street_play(call: types.CallbackQuery, state: FSMContext):
    """Прои виборі категорії Вулиця, функція отримає іменник з його гендером та зберігає у стані
    AnswearState.street_play_start. Після чого користувачу відображається слово та клавіатура"""
    await AnswearState.street_play_start.set()          # Set state зберігає стан
    results = await get_word_from_url(category_word(call.data)) # JSON відповідь з бази данних
    res = random.choice(results)
    print(call.data)
    async with state.proxy() as data:
        data["step"] = 1
        data["answer"] = res.get("gender")
        data['word'] = res.get("word")
        await call.message.answer(f"{data['step']}/10. Якого роду слово -  {data['word']}", reply_markup=inline_kb)


"""Порівнює відповідь користувача, зі словом з БД, яке надійшло раніше.
     Перевіряє скільки слів відповів користувач."""
@dp.callback_query_handler(lambda c: c.data in ["das", "die", "der"], state=AnswearState.street_play_start)
async def send_random_value(call: types.CallbackQuery, state: FSMContext):
    answer = call.data  #те що відповів користувач
    async with state.proxy() as data:
        print(f"відповідь {answer}")
        if answer == data.get("answer"):
            res = await get_word_from_url(result_call)
            random_resalt = random.choice(res)
            data["step"] += 1
            data["answer"] = random_resalt.get("gender")
            data["word"] = random_resalt.get("word")
            if data["step"] > 10:
                await call.message.answer( "The game is over", reply_markup=reapeat_button)
                await state.finish()
            else:
                await call.message.answer(
                                      f"{random.choice(RichtigMessage)}  \n {data['step']}/10.  {data['word']}", reply_markup=inline_kb)
        else:
            await call.message.answer(f"{random.choice(FalschMessage)} \n", reply_markup=inline_kb)


