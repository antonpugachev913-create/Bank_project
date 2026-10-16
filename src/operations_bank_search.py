import re
from collections import Counter


def filter_bank_search(bank_operations: list[dict], search: str) -> list[dict]:
    """Функция, возвращающая словари, которые имеют в описании строку search"""
    try:
        if not isinstance(bank_operations, list) or not isinstance(search, str):
            print("Вы ввели неверные данные")
            raise TypeError
        filtered_bank_operations = []
        for operation in bank_operations:
            text = operation.get("description", "")
            if isinstance(text, str) and re.search(search, text):
                filtered_bank_operations.append(operation)
        return filtered_bank_operations

    except TypeError as type_error:
        raise type_error
    except Exception as error:
        print(f"Произошла ошибка {error}")
        raise Exception


def count_bank_operations(
    bank_operations: list[dict], categories: list
) -> dict[str, int]:
    """Функция считает, сколько раз каждая категория встречается в списке операций."""
    if not isinstance(bank_operations, list) or not isinstance(categories, list):
        print("Вы ввели неверные данные")
        raise TypeError

    help_list = []
    for operation in bank_operations:
        category = operation.get("description", "")
        if category in categories:
            help_list.append(category)
    counted_categories_operations = Counter(help_list)

    for category in categories:
        if category not in counted_categories_operations:
            counted_categories_operations[category] = 0

    return dict(counted_categories_operations)
