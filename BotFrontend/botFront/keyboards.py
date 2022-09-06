from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

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

    InlineKeyboardButton("Street", callback_data="street"),
    InlineKeyboardButton("Home", callback_data="home"),
    InlineKeyboardButton("Food", callback_data="food"),
    ]

inline_kb_cat = InlineKeyboardMarkup(row_width=3)
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
