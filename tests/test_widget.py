import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "show, mask",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(show, mask):
    assert mask_account_card(show) == mask


def test_mask_account_card_type():
    with pytest.raises(TypeError):
        assert mask_account_card((123, 12332))


def test_mask_account_card_zero():
    assert mask_account_card("")


def test_get_date(dates):
    assert get_date("2024-03-11T02:26:18.671407") == dates
    assert get_date("")


def test_get_date_diff_len(dates):
    assert get_date("2024-03-11T02:26:18.6714072121211212") == dates
    assert get_date("2024-03-1") == "Incorrect date"


def test_get_date_cl():
    assert get_date(123) == 0
    assert get_date([]) == 0
