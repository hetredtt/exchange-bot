from dispatcher import bot, dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
import ExchangeModule.service as Service
from utils.logger import ModuleLogger

logger = ModuleLogger(__name__).get_logger()

@dp.message_handler(commands="convert")
async def convert(message: Message):
    logger.info(f"User {message.chat.id} press {message.text}")
    command_parts = message.text.split()
    await Service.convert(bot, message, command_parts)

@dp.message_handler(commands="codes")
async def codes(message: Message):
    logger.info(f"User {message.chat.id} view codes")
    await Service.codes(bot, message)
