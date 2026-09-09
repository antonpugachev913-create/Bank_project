def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера карты"""
    num = ""
    ans = []
    for i in range(1, 17):
        if 6 < i < 13:
            num += "*"
        else:
            num += number[i - 1]
        if i % 4 == 0:
            ans.append(num)
            num = ""
    a = " ".join(ans)
    return a


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"** {number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
