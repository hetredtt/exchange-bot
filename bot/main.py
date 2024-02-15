from aiogram import executor
from dispatcher import dp
import MenuModule.controller, ExchangeModule.controller, SpeakerModule.controller

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)