import json


def open_json(file_path: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    try:
        with open(file_path, encoding="utf-8") as json_file:
            trans = json.load(json_file)
        return trans
    except Exception:
        return []



