from aiogram import executor
from botFront.app import dp


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
