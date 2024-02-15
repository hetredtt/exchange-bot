from utils.keywords import hello_list, bye_list, neutral_phrases
import random

async def message(bot, message):
    user_text = message.text
    lower_user_text = user_text.lower()
    if lower_user_text in bye_list:
        random_number = random.randint(0, len(bye_list))
        await bot.send_message(chat_id=message.chat.id, text=bye_list[random_number])
    elif lower_user_text in hello_list:
        random_number = random.randint(0, len(hello_list))
        await bot.send_message(chat_id=message.chat.id, text=hello_list[random_number])
    else:
        random_number = random.randint(0, len(neutral_phrases))
        await bot.send_message(chat_id=message.chat.id, text=neutral_phrases[random_number])