import requests
from os import getenv
from typing import Any
from dotenv import load_dotenv

load_dotenv()
API_KEY = getenv('API_KEY')


def get_total_transaction(transaction: dict[str, Any]) -> float:
    amount = float(transaction["operationAmount"]["amount"])
    type_transaction = transaction["operationAmount"]["currency"]["code"]
    if type_transaction == "RUB":
        return amount
    else:
        url = 'https://api.apilayer.com/exchangerates_data/convert'
        payload = {
            "amount": f'{amount}',
            "from": f'{type_transaction}',
            "to": "RUB"
        }

        headers = {
            'apikey': API_KEY
        }


        response = requests.get(url, headers=headers, params=payload, timeout=5)
        res = response.json()
        return res

tr =    {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
print(get_total_transaction(tr))


