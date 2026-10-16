from unittest.mock import patch
import pytest
from src.main import main


def test_main_scenario(monkeypatch, capsys):
    inputs = ["1", "executed", "да", "по возрастанию", "нет", "нет"]
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))

    with patch("src.main.get_transaction_information", return_value=[]):
        main()

    captured = capsys.readouterr().out
    assert "Привет! Добро пожаловать" in captured
    assert "Не найдено ни одной транзакции" in captured
