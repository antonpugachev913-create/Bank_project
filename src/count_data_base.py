import pandas as pd
import pathlib
def count_data_from_csv(way:str | None=None) -> str:
     file_path = pathlib.Path(__file__).parent.parent / way
     transactions_df = pd.read_csv(file_path, sep=';')
     return transactions_df.to_json(orient='records', indent=4)

print(count_data_from_csv('data/transactions.csv'))


def count_data_from_excel(way: str | None = None) ->  str:
