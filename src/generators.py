from typing import Any
from collections.abc import Iterator

def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Функция, возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for operation in transactions:
        if operation["operationAmount"]["currency"]["name"] == currency and operation["operationAmount"]["currency"]["code"] == currency:
            yield operation

test = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "61521.13",
            "currency": {"name": "руб.", "code": "RUB"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]

for i in range(3):
    print(next(filter_by_currency(test, 'USD')))


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for operation in transactions:
        yield operation["description"]


descriptions = transaction_descriptions(test)
for _ in range(5):
    print(next(descriptions, 'End'))

#
# def card_number_generator(start: int, end : int):
#     """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX """
#     for char
#
#
#
# for card_number in card_number_generator(1, 5):
#     print(card_number)

