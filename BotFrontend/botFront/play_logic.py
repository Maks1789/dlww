from .app import *
from .player_state import AnswearState
from .local_setting import WORDS_API_URL_Street
from .data_fetcher import get_word_from_url
from .keyboards import inline_kb


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
async def button_click_call_back(callback_query: types.CallbackQuery, state: FSMContext):
    """ Порівнює відповідь користувача, зі словом з БД, яке надійшло раніше.
     Перевіряє скільки слів відповів користувач. """
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get("answer"):
            res = await get_random() #!!! треба змінити!
            data["step"] += 1
            data["answer"] = res.get("gender")
            data["word"] = res.get("word")
            if data["step"] > 10:
                await bot.send_message(callback_query.from_user.id, "The game is over",)
                await AnswearState.street_play_start.set()
            else:
                await bot.send_message(callback_query.from_user.id,
                                       "Richtig  \n" + f"{data['step']}/10.  {data['word']}", reply_markup=inline_kb)

        else:
            await bot.send_message(callback_query.from_user.id,
                                   "Leider nein. Versuchen Sie noch mal! \n", reply_markup=inline_kb)
