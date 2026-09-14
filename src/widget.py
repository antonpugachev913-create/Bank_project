def mask_account_card(data : str) -> str:
    """Функция маскировки номера карты и счета"""
    data = data.split()
    name = ''
    number = ''
    for char in data:
        if char.isalpha():
            name = name + char + ' '
        else:
            number += char
    name = name.split()
    final_name = ' '.join(name)
    if final_name == 'Счет':
        return f"Счет **{number[-4:]}"
    else:
        return f'{final_name} {number[:4]} {number[4:6]}** **** {number[12:]}'


# print(mask_account_card('Счет 73654108430135874305'))
# print(mask_account_card('Visa Platinum 7000792289606361'))
# print(mask_account_card('Maestro 1596837868705199'))


def get_date(date : str) -> str:
    """Функция, изменяющая формат даты"""
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    ans = f'{day}.{month}.{year}'
    return ans

print(get_date("2024-03-11T02:26:18.671407"))