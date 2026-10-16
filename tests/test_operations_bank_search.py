import pytest

from src.operations_bank_search import count_bank_operations, filter_bank_search
from tests.conftest import bank_data


def test_filter_bank_search(bank_data) -> None:
    assert filter_bank_search(bank_data, "Перевод организации") == [
        {
            "amount": 16210,
            "currency_code": "RUB",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Card 1234",
            "id": 650703,
            "state": "EXECUTED",
            "to": "Account 5678",
        }
    ]
    assert filter_bank_search(bank_data, "Перевод") == [
        {
            "amount": 16210,
            "currency_code": "RUB",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Card 1234",
            "id": 650703,
            "state": "EXECUTED",
            "to": "Account 5678",
        },
        {
            "amount": 30368,
            "currency_code": "RUB",
            "date": "2023-07-22T05:02:01Z",
            "description": "Перевод физическому лицу",
            "from": "Account 1111",
            "id": 593027,
            "state": "CANCELED",
            "to": "Account 2222",
        },
    ]


def test_filter_bank_search_errors(bank_data) -> None:
    banks_data = tuple(bank_data)
    bad_bank_data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "amount": 5000},
    ]
    with pytest.raises(TypeError):
        assert filter_bank_search(banks_data, "Перевод")
        assert filter_bank_search(bank_data, 1234)
    # with pytest.raises(Exception):
    #     assert filter_bank_search(bad_bank_data, "Перевод")


def test_count_bank_operations(bank_data, categories) -> None:

    expected_result = {
        "Перевод организации": 1,
        "Покупка в интернет-магазине": 1,
        "Открытие вклада": 0,
    }
    assert count_bank_operations(bank_data, categories) == expected_result


def test_count_bank_operations_errors(bank_data, categories) -> None:
    banks_data = tuple(bank_data)
    with pytest.raises(TypeError):
        count_bank_operations(banks_data, categories)
        count_bank_operations(bank_data, 1234)
