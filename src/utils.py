import json
import logging
from json import JSONDecodeError, load
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE_PATH = BASE_DIR / "logs" / "masks.log"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOG_FILE_PATH, mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_information(way):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger.info("Начало работы")
    try:
        file_path = Path(way)
        if not file_path.exists() or file_path.stat().st_size == 0:
            logger.warning("Такого файла не существует или он пустой")
            return []
        with open(way, "r", encoding="utf-8") as file:
            out = load(file)
            if not isinstance(out, list):
                logger.warning("Неверный тип данных, проверьте свой ввод")
                return []
            logger.info("Возвращаем данные в виде словаря")
            return out
    except json.JSONDecodeError:
        logger.error(f"Произошла ошибка {JSONDecodeError}, проверьте ваш json файл")
        return []
