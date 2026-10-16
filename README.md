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

```decorators.py```
Содержит декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.

```count_data_base.py```
Содержит функции, который позволяют считывать данные о транзакциях в форматах: csv, xlsx.

```operations_bank_search.py```
Содержит функции, фильтрующие словари по ключевому слову и считающие кол-во операций в словаре из заданных категорий

```main.py```
Содержит основную функцию, которая объединяет все модули проекта в единое целое
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

## Примеры использования генераторов (decorators.py):
#### 1. Логирование начала и конца выполнения функции
```python
from src.decorators import log

#Пример запуска

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
```


## Примеры использования функций чтения из форматов csv, xlsx (count_data_base.py):
#### 1. Cчитывание данных из формата csv
```python
data = count_data_from_csv('ваш путь до файла')
print(data) # вывести результат
```

#### 2. Cчитывание данных из формата xlsx
```python
data = count_data_from_excel('ваш путь до файла')
print(data) # вывести результат
```

## Примеры использования функций фильтрация и подсчета банковских транзакций (operations_bank_search.py):
#### 1. Фильтрация по ключевому слову
```python
bank_operations = [your data]
search = your_key_word
filtered_transaction = filter_bank_search(bank_operations, search)
print(filtered_transaction) #выводим результат
```
#### 2. Подсчет операций из вашего словаря с заданными категориями
```python
bank_operations = [your data]
categories = [your categories]
res = count_bank_operations(bank_operations, categories)
print(res) # вывести результат
```

##  Работа с главным модулем программы (`main.py`):
Запуск интерактивного консольного приложения:
```bash
poetry run python src/main.py
```

### Основные этапы работы программы:
1. **Выбор источника данных:** Пользователь выбирает формат входного файла (JSON, CSV или XLSX).
2. **Фильтрация по статусу:** Запрос желаемого статуса транзакций (`EXECUTED`, `CANCELED`, `PENDING`) с автоматическим приведением к регистру.
3. **Сортировка по дате:** Выбор сортировки (Да/Нет) и направления (По возрастанию / По убыванию).
4. **Валютный фильтр:** Возможность оставить строго рублёвые операции (`RUB`).
5. **Текстовый фильтр:** Фильтрация результирующего списка по ключевому слову в описании.
6. **Вывод результатов:** Отображение количества подходящих транзакций и вывод замаскированных данных с выводом финальных сумм в рублях.
```
```
