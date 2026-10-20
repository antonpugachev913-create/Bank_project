from os import getenv
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = getenv("API_KEY")


def get_total_transaction(transaction: dict[str, Any]) -> float:
    """Принимает транзакцию (из JSON, CSV или Excel) и возвращает сумму в рублях,

    при необходимости конвертируя валюту через API.
    """
    if not transaction or not isinstance(transaction, dict):
        return 0.0

    if "operationAmount" in transaction and isinstance(
        transaction["operationAmount"], dict
    ):
        raw_amount = transaction["operationAmount"].get("amount", 0)
        currency_code = (
            transaction["operationAmount"].get("currency", {}).get("code", "RUB")
        )
    else:
        raw_amount = transaction.get("amount", 0)
        currency_code = transaction.get("currency_code", "RUB")

    try:
        amount = float(raw_amount)
    except (ValueError, TypeError):
        return 0.0

    if currency_code == "RUB":
        return amount

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {"amount": str(amount), "from": str(currency_code), "to": "RUB"}
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, params=payload, timeout=5)
        if response.status_code == 200:
            res = response.json()
            return float(res.get("result", 0.0))
        else:
            print(f"Ошибка API (Статус {response.status_code})")
            return 0.0
    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        return 0.0
