@echo off
:: Переключаем кодировку консоли Windows на UTF-8, чтобы русский текст отображался корректно
chcp 65001 > nul

echo ==========================================
echo 🚀 Запуск автоматической проверки кода...
echo ==========================================

echo.
echo [1/5] 🔄 Сортировка импортов через isort...
poetry run isort src/ tests/

echo.
echo [2/5] 🎨 Форматирование кода через Black...
poetry run black src/ tests/

echo.
echo [3/5] 🔍 Проверка стиля через Flake8...
poetry run flake8 src/ tests/

echo.
echo [4/5] 🎯 Проверка аннотаций типов через Mypy...
poetry run mypy src/ tests/

echo.
echo [5/5] 🧪 Запуск тестов через Pytest...
poetry run pytest

echo.
echo ==========================================
echo 🎉 Проверка полностью завершена!
echo ==========================================
pause
