from os import getenv
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = getenv("API_KEY")


def get_total_transaction(transaction: dict[str, Any]) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount = float(transaction["operationAmount"]["amount"])
    type_transaction = transaction["operationAmount"]["currency"]["code"]
    if type_transaction == "RUB":
        return amount
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"amount": f"{amount}", "from": f"{type_transaction}", "to": "RUB"}

        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, params=payload, timeout=5)
        res = response.json()
        return float(res["result"])
