def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера карты"""
    if not isinstance(number, str):
        raise TypeError
    if len(number) != 16:
        return 'Incorrect length string'
    return f'{number[:4]} {number[4:6]}** **** {number[12:]}'


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if not isinstance(number, str):
        raise TypeError
    # if len(number) != 16:
    #     return 'Incorrect length string'
    return f"** {number[-4:]}"

