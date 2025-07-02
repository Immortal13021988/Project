from typing import Generator


def filter_by_currency_new(transactions: list, name: str = "USD", currency_code: int = 2) -> list:
    """Функция возвращает список транзакции, с необходимыми значениями валюты"""
    new_list = []
    for item in transactions:
        if currency_code == 1:
            if item["operationAmount"]["currency"]["code"] == name:
                new_list.append(item)
        elif currency_code == 2:
            if item["currency_code"] == name:
                new_list.append(item)
    return new_list


def filter_by_currency(transactions: list, name: str = "USD") -> Generator:
    """Функция возвращает транзакции, с необходимым значением валюты поочереди"""
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == name:
            yield item


def transaction_descriptions(transactions: list) -> Generator:
    """Функция возвращает описание каждой транзакции поочереди"""
    for item in transactions:
        yield item["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)  # Добавление нолей (приведение к нужному формату)
        """card_number = '0'*(16 - len(str(number))) + str(number) (Еще один вариант приведение к нужному формату"""
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
