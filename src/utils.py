import json
from typing import Any
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_json(file_path: str) -> list[Any]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    try:
        logger.info(f'Выполняем открытия JSON-файла')
        with open(file_path, encoding="utf-8") as json_file:
            trans = json.load(json_file)
        logger.info(f'Проверяем соответствие содержимого файла')
        if type(trans) is list:
            logger.info(f'Проверка файла прошла успешно')
            return trans
        else:
            logger.error(f'Проверка файла провалена (содержимое файла не соответствует)')
            return []
    except (json.JSONDecodeError, FileNotFoundError) as ex:
        logger.error(f'Произошла ошибка: {ex}')
        return []
