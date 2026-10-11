import json
from json import dumps
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_transaction_information


@patch("src.utils.Path.exists", return_value=True)
@patch("src.utils.Path.stat")
def test_utils(mock_stat, mock_exists, transaction):
    mock_stat.return_value.st_size = 100

    json_data = dumps(transaction)

    with (
        patch("builtins.open", mock_open(read_data=json_data)),
        patch("src.utils.load", return_value=transaction),
    ):
        result = get_transaction_information("data/operations.json")

    assert result == transaction


@patch("src.utils.Path.exists", return_value=False)
def test_not_file_utils(mock_exists):
    res = get_transaction_information("empty.json")
    assert res == []


@patch("src.utils.Path.exists", return_value=True)
@patch("src.utils.Path.stat")
def test_empty_file_utils(mock_stat, mock_exists):
    mock_stat.return_value.st_size = 0
    res = get_transaction_information("test.json")
    assert res == []


@patch("src.utils.Path.exists", return_value=True)
@patch("src.utils.Path.stat")
def test_break_file_utils(mock_stat, mock_exists):
    mock_stat.return_value.st_size = 100
    with (
        patch("builtins.open", mock_open(read_data="invalid_json")),
        patch("src.utils.load", side_effect=json.JSONDecodeError("Ошибка", "doc", 0)),
    ):
        result = get_transaction_information("broken.json")
    assert result == []
