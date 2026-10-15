import re
from pprint import pprint

from _collections import defaultdict


def filter_bank_search(bank_operations: list[dict], search: str) -> list[dict]:
    """Функция, возвращающая словари, которые имеют в описании строку search"""
    try:
        if not isinstance(bank_operations, list) or not isinstance(search, str):
            print('Вы ввели неверные данные')
            raise TypeError
        filtered_bank_operations = []
        for operation in bank_operations:
            text = operation["description"]
            if re.search(search, text):
                filtered_bank_operations.append(operation)
        return filtered_bank_operations

    except TypeError as type_error:
        raise type_error
    except Exception as error:
        print(f'Произошла ошибка {error}')
        raise Exception


def count_bank_operations(bank_operations: list[dict], categories: list) -> dict[str: float]:
    if not isinstance(bank_operations, list) or not isinstance(categories, list):
        print('Вы ввели неверные данные')
        raise TypeError
    counted_categories_operations = defaultdict(int)

    for category in categories:
        counted_categories_operations[category] = 0

    for operation in bank_operations:
        category = operation['description']
        if category in categories:
            counted_categories_operations[operation['description']] += 1
    return counted_categories_operations