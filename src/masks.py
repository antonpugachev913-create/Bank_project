import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE_PATH = BASE_DIR / "logs" / "masks.log"

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOG_FILE_PATH, mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера карты"""
    logger.info("Начинаем маскировку номера карты")

    if not isinstance(number, str):
        logger.error("Произошла {TypeError}")
        raise TypeError

    if len(number) != 16:
        logger.warning("Задана неверная длина строки")
        return "Incorrect length string"
    logger.info("Возвращаем маскированный номер карты и завершаем работу")
    return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info("Начинаем маскировку номера карты или счета")
    if not isinstance(number, str):
        logger.error(f"Произошла {TypeError}")
        raise TypeError
    logger.info("Возвращаем маскированный номер карты или счета и завершаем работу")
    return f"** {number[-4:]}"

