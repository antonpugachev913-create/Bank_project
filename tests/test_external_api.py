import json
from json import dumps
from unittest.mock import mock_open, patch

import pytest

from src.external_api import get_total_transaction


def test_external_api_rub():
    tr = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
    assert get_total_transaction(tr) == 31957.58


@patch("requests.get")
def test_external_api_alt_val(mock_response):
    trans = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response.return_value = mock_response
    mock_response.json.return_value = {"result": 793362.21}
    assert (get_total_transaction(trans)) == 793362.21
