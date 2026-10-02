from collections.abc import Iterator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]], currency: str = ""
) -> Iterator[dict[str, Any]]:
    """Функция, возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for operation in transactions:
        try:
            if operation["operationAmount"]["currency"]["code"] == currency:
                yield operation
        except KeyError:
            continue


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for operation in transactions:
        yield operation["description"]


#
def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, end + 1):
        str_num = str(num)
        length = len(str_num)
        card_num = ("0" * (16 - length)) + str_num
        final_num = f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:]}"
        yield final_num


for card_number in card_number_generator(1, 5):
    print(card_number)
