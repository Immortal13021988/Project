import csv
from typing import Any
import pandas as pd


def open_csv(file_path: str) -> list[Any]:
    """
    Функция, которая принимает на вход путь до CSV-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    list_trans = []
    try:
        with open(file_path, encoding="utf-8") as csv_file:
            trans = csv.DictReader(csv_file, delimiter=";")
            for row in trans:
                list_trans.append(row)
        return list_trans
    except (Exception, FileNotFoundError):
        return list_trans


def open_xlsx(file_path: str) -> (pd.DataFrame, str):
    """
        Функция, которая принимает на вход путь до CSV-файла и возвращает список словарей
        с данными о финансовых транзакциях
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except (Exception, FileNotFoundError) as ex:
        return f'Ошибка: {ex}'
