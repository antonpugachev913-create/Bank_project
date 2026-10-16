from src.count_data_base import count_data_from_csv, count_data_from_excel
from src.utils import get_transaction_information


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        number = input().lower()
        if number not in ["1", "2", "3"]:
            print("Вы ввели неверные данные, повторите попытку")
        else:
            number = int(number)
            if number == 1:
                point = "JSON-файл"
                transactions = get_transaction_information("data/operations.json")
            elif number == 2:
                point = "CSV-файл"
                transactions = count_data_from_csv("data/transactions.csv")
            else:
                point = "XLSX-файл"
                transactions = count_data_from_excel("data/transactions_excel.xlsx")

            print(f"Для обработки выбран {point}.")
            break

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        available_status = ["executed", "canceled", "pending"]
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        stat = input()
        status = stat.lower()
        if status in available_status:
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{stat}" недоступен, повторите попытку.')

    # 3. Последующие шаги обработки
    print("Отсортировать операции по дате? Да/Нет")
    # Тут будет ввод пользователя и обработка сортировки по дате

    print("Отсортировать по возрастанию или по убыванию?")
    # Тут будет ввод пользователя и обработка направления сортировки

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    # Тут будет ввод пользователя и фильтрация по ключевому слову

    print("Распечатываю итоговый список транзакций...")
    # Тут будет итоговый вывод результатов


if __name__ == "__main__":
    main()
