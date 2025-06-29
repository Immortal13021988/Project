import pandas as pd


def open_csv(file_path: str) -> list:
    """
    Функция, которая принимает на вход путь до CSV-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    try:
        df = pd.read_csv(file_path, delimiter=";")
        return df.to_dict("records")
    except (Exception, FileNotFoundError):
        return []


def open_xlsx(file_path: str) -> list:
    """
    Функция, которая принимает на вход путь до XLSX-файла и возвращает список словарей
    с данными о финансовых транзакциях
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict("records")
    except (Exception, FileNotFoundError):
        return []
