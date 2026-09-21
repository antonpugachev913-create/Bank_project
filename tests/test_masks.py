import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_correct_mask_card(nums_card):
    assert get_mask_card_number(nums_card) == '7000 79** **** 6361'
    with pytest.raises(TypeError):
         assert get_mask_card_number(123)
    with pytest.raises(TypeError):
        assert get_mask_card_number([1, 2, 3, 4, 5])

def test_correct_mask_card_len():
    assert get_mask_card_number("70007922896063611") == 'Incorrect length string'
    assert get_mask_card_number('') == 'Incorrect length string'

@pytest.mark.parametrize('show, mask', [('73654108430135874305', '** 4305'),
                                         ('71235108430135875252', '** 5252')
                                         ])

def test_correct_mask_account(show, mask):
    assert get_mask_account(show) == mask

def test_correct_mask_account_len():
    assert get_mask_account('12234') == '** 2234'
    assert get_mask_account('712351084301358752522132132131232132131') == '** 2131'


def test_correct_mask_account_type():
    with pytest.raises(TypeError):
         assert get_mask_account(True)
    with pytest.raises(TypeError):
         assert get_mask_account({1:2, 2:3})
