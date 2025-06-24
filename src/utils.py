import json
from typing import Any


def open_json(file_path: str) -> list[Any]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    try:
        with open(file_path, encoding="utf-8") as json_file:
            trans = json.load(json_file)
        if type(trans) is list:
            return trans
        else:
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
