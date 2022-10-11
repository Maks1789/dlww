import random

from aiogram.dispatcher import FSMContext

from .app import *
from .bot_messages import RichtigMessage, FalschMessage
# from .app import *
from .data_fetcher import get_word_from_url
from .keyboards import sens_button, get_keyboard
from .local_setting import SENTENCES_API_URL
from .player_state import AnswearState


def right_answer(answer_to_send):
    "Answear 1"
    answer_one = answer_to_send[0].split()[3]
    correkt_answer_one = answer_to_send[0].split()[4]
    "Answear 2"
    answer_two = answer_to_send[1].split()[3]
    correkt_answer_two = answer_to_send[1].split()[4]
    "Änswear 3"
    answer_tree = answer_to_send[2].split()[3]
    correkt_answer_tree = answer_to_send[2].split()[4]
    return answer_one, answer_two, answer_tree, correkt_answer_one, correkt_answer_two, correkt_answer_tree


@dp.callback_query_handler(text="sentence", state="*")
async def send_sentence_value(call: types.CallbackQuery, state: FSMContext):
    '''Показує речення та варіанти відповіді після чого користувач має вибрати правильну відповідь'''
    await AnswearState.street_play_start.set()  # Set state зберігає стан
    res = await get_word_from_url(SENTENCES_API_URL)  # class li Отримує питання
    random_res = random.choice(res)  # Обирае рандомне питання З ВІДПОВІДЯМИ
    question_to_send = random_res.get("question_fild")  # ВІДОКРЕМЛЮЄ ПИТАННЯ
    answer_sep = list(right_answer(random_res.get("answer")))  # розбиває питання і правильні відповіді

    async with state.proxy() as data:
        data["step"] = 1
        data["answer"] = "True"
        data['question'] = question_to_send

    await call.message.answer(f"{question_to_send}", reply_markup=f"{get_keyboard(*answer_sep)}")


@dp.callback_query_handler(lambda c: c.data in ["True", "False"], state=AnswearState.street_play_start)
async def send_random_value(call: types.CallbackQuery, state: FSMContext):
    answer = call.data  # те що відповів користувач
    print(answer)
    async with state.proxy() as data:
        print(f"відповідь {answer}")
        if answer == data.get("answer"):
            res = await get_word_from_url(SENTENCES_API_URL)  # class li Отримує питання
            random_res = random.choice(res)  # Обирае рандомне питання З ВІДПОВІДЯМИ
            question_to_send = random_res.get("question_fild")  # ВІДОКРЕМЛЮЄ ПИТАННЯ
            answer_sep = list(right_answer(random_res.get("answer")))  # розбиває питання і правильні відповіді
            ans_key = get_keyboard(*answer_sep)
            data["step"] += 1
            data["answer"] = "True"
            data["word"] = question_to_send
            if data["step"] > 10:
                await call.message.answer("The game is over", reply_markup=sens_button)
                await state.finish()
            else:
                await call.message.answer(
                    f"{random.choice(RichtigMessage)}  \n {data['step']}/10.  {data['word']}",
                    reply_markup=ans_key)
        else:
            await call.message.answer(f"{random.choice(FalschMessage)} \n")
