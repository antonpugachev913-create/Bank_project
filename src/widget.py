def mask_account_card(data: str) -> str:
    if not isinstance(data, str):
        raise TypeError
    """Функция маскировки номера карты и счета"""
    data = data.split()
    name = ""
    number = ""
    for char in data:
        if char.isalpha():
            name = name + char + " "
        else:
            number += char
    name = name.split()
    final_name = " ".join(name)
    if final_name == "Счет":
        return f"Счет **{number[-4:]}"
    else:
        return f"{final_name} {number[:4]} {number[4:6]}** **** {number[12:]}"


def get_date(date: str) -> str:
    """Функция, изменяющая формат даты"""
    if not isinstance(date, str):
        return 0
    if len(date) < 10:
        return "Incorrect date"
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    ans = f"{day}.{month}.{year}"
    return ans
