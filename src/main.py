from src.count_data_base import count_data_from_csv, count_data_from_excel
from src.external_api import get_total_transaction
from src.operations_bank_search import filter_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transaction_information
from src.widget import get_date, mask_account_card


def main():
    """Функция, которая объединяет все модули проекта в 1 целое"""
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
            filtered_transactions = filter_by_state(transactions, status)
            print(filtered_transactions)
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{stat}" недоступен, повторите попытку.')

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        sort_flag = input().lower()
        if sort_flag in ["да", "нет"]:
            if sort_flag == "да":
                while True:
                    print("Отсортировать по возрастанию или по убыванию?")
                    flag = input().lower()
                    available_flags = ["по возрастанию", "по убыванию"]
                    if flag in ["по возрастанию", "по убыванию"]:
                        if flag == "по возрастанию":
                            sorted_date_transactions = sort_by_date(
                                filtered_transactions, False
                            )
                        else:
                            sorted_date_transactions = sort_by_date(
                                filtered_transactions, True
                            )
                        break
                    else:
                        print(
                            f"Вы ввели неверные данные, введите {' '.join(available_flags)}"
                        )
            else:
                sorted_date_transactions = filtered_transactions
            break
        else:
            print("Вы ввели неверные данные, повторите попытку!")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        rub_flag = input().lower()
        if rub_flag in ["да", "нет"]:
            if rub_flag == "нет":
                cur_data_transactions = sorted_date_transactions
            else:
                cur_data_transactions = []
                for op in sorted_date_transactions:
                    if not isinstance(op, dict):
                        continue
                    if "operationAmount" in op and isinstance(
                        op["operationAmount"], dict
                    ):
                        currency = op["operationAmount"].get("currency", {}).get("code")
                    else:
                        currency = op.get("currency_code")

                    if currency == "RUB":
                        cur_data_transactions.append(op)
            break
        else:
            print("Вы ввели неверные данные, повторите попытку!")

    while True:
        print(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
        )
        filter_trans_flag = input().lower()
        if filter_trans_flag in ["да", "нет"]:
            if filter_trans_flag == "нет":
                final_data_transactions = cur_data_transactions
                break
            else:
                while True:
                    print("Введите ключевое слово")
                    key_word = input().lower()
                    if len(key_word) > 0:
                        final_data_transactions = filter_bank_search(
                            cur_data_transactions, key_word
                        )
                        break
                    else:
                        print("Вы ввели пустое слово, повторите попытку")
        else:
            print("Вы ввели неверные данные, введите Да или Нет")

    print("Распечатываю итоговый список транзакций...")
    if len(final_data_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        le = len(final_data_transactions)
        print(f"Всего банковских операций в выборке: {le}")

        for data_transaction in final_data_transactions:
            date = data_transaction.get("date", "")
            transaction_description = data_transaction.get("description", "")
            trans_date = get_date(date)
            print(f"{trans_date} {transaction_description}")

            account_card_from = mask_account_card(data_transaction.get("from", ""))
            account_card_to = mask_account_card(data_transaction.get("to", ""))

            if account_card_from == "":
                print(account_card_from)
            else:
                print(f"{account_card_from} -> {account_card_to}")

            amount = get_total_transaction(data_transaction)
            print(amount)
            print()


if __name__ == "__main__":
    main()
