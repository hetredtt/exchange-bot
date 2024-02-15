import utils.api_query as ApiQuery

async def convert(bot, message, command_parts):
    if len(command_parts) < 5:
        await bot.send_message(chat_id=message.chat.id, text="Вы обделили меня необходимыми данными для поиска")
    else:
        res = await ApiQuery.convert(command_parts[3], command_parts[5], command_parts[1])

        await bot.send_message(chat_id=message.chat.id, text=f"Результат конвертации валют: {res}")

async def codes(bot, message):
    codes = await ApiQuery.codes()
    code_text = ""
    for elem in codes['codes']:
        code_text = code_text + elem['code'] + " - " + elem['name'] +"\n"
    await bot.send_message(chat_id=message.chat.id, text=code_text)
