import requests

async def convert(code_from, code_to, amount):
    url = "https://api.apilayer.com/currency_data/convert"

    params = {
        'amount': amount,
        'from': code_from,
        'to': code_to
    }
    headers= {
    "apikey": "6XEGKOzrnul8W49oxoUrFP72XuLP4g6N"
    }

    response = requests.request("GET", url, headers=headers, params = params)

    return response.json()['result']

async def codes():
    url = "http://127.0.0.1:7050/code/list"
    response = requests.get(url)
    data = response.json()
    return data
