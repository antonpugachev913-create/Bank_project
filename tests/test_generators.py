import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(check_filter):
    usd_iterator = filter_by_currency(check_filter, "USD")
    assert next(usd_iterator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_iterator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_iterator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_zero(check_filter):
    usd_iterator = filter_by_currency(check_filter, "OMG")
    assert next(usd_iterator, "Bad") == "Bad"
    assert next(usd_iterator, "Bad") == "Bad"


def test_filter_no():
    usd_iterator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(usd_iterator)


def test_transaction_descriptions(check_filter):
    us_iterator = transaction_descriptions(check_filter)
    assert next(us_iterator) == "Перевод организации"
    assert next(us_iterator) == "Перевод со счета на счет"
    assert next(us_iterator) == "Перевод со счета на счет"


def test_transaction_descriptions_size():
    us_iterator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(us_iterator)


@pytest.mark.parametrize(
    "index, another",
    [
        (0, "Перевод другу"),
        (1, "Оплата подписки"),
        (2, "Покупка продуктов"),
        (3, "Выплата зарплаты"),
        (4, "Описание отсутствует"),
    ],
)
def test_transaction_description_big(index, another, description):
    text = description[index]
    usd_iterator = transaction_descriptions([text])
    assert next(usd_iterator) == another


def test_card_number_generator():
    iterator = card_number_generator(1, 5)
    assert next(iterator) == "0000 0000 0000 0001"
    assert next(iterator) == "0000 0000 0000 0002"
    assert next(iterator) == "0000 0000 0000 0003"
    assert next(iterator) == "0000 0000 0000 0004"
    assert next(iterator) == "0000 0000 0000 0005"
    assert next(iterator, "Bad") == "Bad"
