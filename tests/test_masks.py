import pytest
from src.masks import get_mask_card_number

def test_correct_mask_card():
    assert get_mask_card_number("7000792289606361") == '7000 79** **** 6361'
    with pytest.raises(TypeError):
         assert get_mask_card_number(123)
    with pytest.raises(TypeError):
        assert get_mask_card_number([1, 2, 3, 4, 5])

def test_correct_mask_card_len():
    assert get_mask_card_number("70007922896063611") == 'Incorrect length string'
    assert get_mask_card_number('') == 'Incorrect length string'

    # print(get_mask_account("73654108430135874305"))