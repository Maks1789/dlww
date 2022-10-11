from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

"""" Початкове меню з 2 кнопок Verben\Дієслова 
Artikel\ Артикль """
button_start= [

    InlineKeyboardButton("Verben\Дієслова", callback_data="Verben"),
    InlineKeyboardButton("Artikel\Артикль", callback_data="Artikel"),
    ]

inline_start_cat = InlineKeyboardMarkup(row_width=2)
inline_start_cat.add(*button_start)





"""Кнопки вибору роду слова (der,die,das )  """
buttons = [

    InlineKeyboardButton("Der", callback_data="der"),
    InlineKeyboardButton("Die", callback_data="die"),
    InlineKeyboardButton("Das", callback_data="das"),
    ]

inline_kb = InlineKeyboardMarkup(row_width=1)
inline_kb.add(*buttons)


"""Кнопки вибору категорії (Їжа, дім, транспорт) inline_kb_cat """
buttons_cat = [

    InlineKeyboardButton(" die Stadt", callback_data="street"),
    InlineKeyboardButton("Wohnen", callback_data="home"),
    InlineKeyboardButton("Essen und Trinken", callback_data="food"),
    ]

inline_kb_cat = InlineKeyboardMarkup(row_width=2)
inline_kb_cat.add(*buttons_cat)

"""Кнопка повторити"""
reapeat_button = InlineKeyboardMarkup(row_width=1)
reapeat_button.add(InlineKeyboardButton(" Щоб повторити, тицьни туточки", callback_data="repeat"))


"""Звичайна кнопка відміна та рестарта
keyboard_cancel_restart = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cancel_button = KeyboardButton(text="cancel")
restart_button = KeyboardButton(text="repeat")
keyboard_cancel_restart.add(cancel_button, restart_button)
"""



"""Кнопка пройти тест"""

sens_button = InlineKeyboardMarkup(row_width=1)
sens_button.add(InlineKeyboardButton(" Щоб почати тест натисни", callback_data="sentence"))


def get_keyboard(answer_one, answer_two, answer_tree, correkt_answer_one, correkt_answer_two, correkt_answer_tree):

    buttons = [

        InlineKeyboardButton(f"{answer_one}", callback_data=f"{correkt_answer_one}"),
        InlineKeyboardButton(f"{answer_two}", callback_data=f"{correkt_answer_two}"),
        InlineKeyboardButton(f"{answer_tree}", callback_data=f"{correkt_answer_tree}"),
    ]

    inline_kb_sent = InlineKeyboardMarkup(row_width=1)
    inline_kb_sent.add(*buttons)

    return inline_kb_sent
