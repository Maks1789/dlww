from aiogram.dispatcher.filters.state import State, StatesGroup


class AnswearState(StatesGroup):
    street_play_start = State()
    street_play = State()
