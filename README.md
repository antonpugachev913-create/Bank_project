from tests.conftest import description

# Название: Bank_project

## Описание:

Bank_project - это проект, который позволяет совершать операции над банковскими счетами и картами (скрывать их номера).

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/antonpugachev913-create/Bank_project.git
```
2. Установите poetry:
```
pip install poetry
```
3. Установите зависимости:
```
poetry install
```

## Тестирование:
1. Запуск тестирования всей программы:
```
poetry run pytest
```
2. Запуск тестирования c покрытием кода:
```
poetry run pytest --cov=src --cov-report=html
```
3. Запуск линтеров и проверки типов:
```
poetry run flake8
poetry run mypy
```
## Документация:
В пакете ```src``` лежат модули кода:

```masks.py```
Содержит функции маскировки карты и счета

```widget.py```
Содержит функцию распознавания карты и счета и в дальнейшем маскирует их

```processing.py``` 
Содержит функции фильтров по дате и статусу

```generators.py```
Содержит функции фильтрации транзакций по валюте, вывода описания транзакций, генерации номера карта для пользователя

## Примеры использования генераторов (generators.py):
#### 1. Фильтрация по валюте (`filter_by_currency`)
```python
from src.generators import filter_by_currency

#Пример запуска
usd_iterator = filter_by_currency(transactions, 'USD')

#Получение следующего элемента
el = next(usd_iterator)
```

#### 2. Вывод  описания транзакций
```python
from src.generators import transaction_descriptions

#Пример запуска
usd_iterator = filter_by_currency(transactions, 'OMG')


#Получение следующего описания
description = next(usd_iterator)
```

#### 3. Генерация номера карты
```python
from src.generators import card_number_generator

#Запуск
iterator = card_number_generator(1, 5)

#Получение следующего номера карты
number =  next(iterator)
```

