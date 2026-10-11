from typing import Any


def filter_by_state(
    dictionaries: list[dict[str, Any]], key: str = "EXECUTED"
) -> list[dict[str, Any]]:
    """Функция возвращающая список словарей,у которых ключ state соответствует указанному значению."""
    if not isinstance(key, str):
        raise TypeError
    new_dict = []
    for d in dictionaries:
        if d["state"] == key:
            new_dict.append(d)
    return new_dict

def sort_by_date(dates: list[dict[str, Any]], res: bool = True) -> list[dict[str, Any]]:
    """Функция возвращающая список словарей, отсортированных по дате"""
    return sorted(dates, key=lambda x: x["date"], reverse=res)
