

async def say_hello(bot, message):
    hello = """
Приветствую, этот бот является тестовым заданием EasyByte.
В его функционал входит конвертация валют, а также приветствие или прощание в зависимости от контекста.
Введите /help для знакомаста в с командами
"""
    await bot.send_message(chat_id=message.chat.id, text=hello)

async def help(bot, message):
    help = """
Команда /convert используется для того чтобы конвертировать сумму из одной валюты в другую.
Пример использования: 
\"/convert 100 from USD to UZS\"
Узнать коды валют можно с помощью команды /codes
"""
    await bot.send_message(chat_id=message.chat.id, text=help)

