def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера карты"""
    return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"** {number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
