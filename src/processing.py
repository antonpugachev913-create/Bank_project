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


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ],
        "CANCELED",
    )
)


def sort_by_date(dates: list[dict[str, Any]], res: bool = True) -> list[dict[str, Any]]:
    """Функция возвращающая список словарей, отсортированных по дате"""
    return sorted(dates, key=lambda x: x["date"], reverse=res)


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)
