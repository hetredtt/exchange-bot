from dispatcher import bot, dp
from aiogram.types import Message
import SpeakerModule.service as Service
from utils.logger import ModuleLogger
from aiogram import types

logger = ModuleLogger(__name__).get_logger()

@dp.message_handler(commands=None, content_types=[types.ContentType.TEXT])
async def message(message: Message):
    logger.info(f"User {message.chat.id} said {message.text}")
    await Service.message(bot, message)