import pathlib

import pandas as pd


def count_data_from_csv(way: str | None = None) -> str:
    file_path = pathlib.Path(__file__).parent.parent / way
    transactions_df = pd.read_csv(file_path, sep=";")
    return transactions_df.to_json(orient="records", indent=4)


# print(count_data_from_csv('data/transactions.csv'))


def count_data_from_excel(way: str | None = None) -> str:
    file_path = pathlib.Path(__file__).parent.parent / way
    transactions_df = pd.read_excel(file_path)
    return transactions_df.to_json(orient="records", indent=4)


print(count_data_from_excel("data/transactions_excel.xlsx"))
