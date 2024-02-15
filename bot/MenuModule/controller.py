from dispatcher import bot, dp
from aiogram.types import Message
import MenuModule.service as Service
from utils.logger import ModuleLogger

logger = ModuleLogger(__name__).get_logger()

@dp.message_handler(commands="start")
async def start(message: Message):
    logger.info(f"User {message.chat.id} pressed /start")
    await Service.say_hello(bot, message)

@dp.message_handler(commands="help")
async def help(message: Message):
    logger.info(f"User {message.chat.id} pressed /help")
    await Service.help(bot, message)
