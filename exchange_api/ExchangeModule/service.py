import requests
from ExchangeModule.model import CodeList

async def code_list():
    url = f"https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    list = []
    for code in data['Valute']:
        code_json = {
            "code": str(code),
            "name": str(data['Valute'][str(code)]['Name'])
        }
        print(code_json)
        list.append(code_json)
    res = CodeList(codes=list)
    return res
