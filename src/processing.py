import re
from collections import Counter
from typing import Any, Dict, List


def filter_by_state(dict_filter: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in dict_filter if item.get("state") == state]


def sort_by_date(sort_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(sort_data, key=lambda x: str(x.get("date")), reverse=reverse)


def process_bank_search(data: list[dict], search: str) -> list:
    """Функцию принимает список словарей с данными о банковских операциях и строку
    поиска, а возвращает список словарей с искомой строкой."""
    try:
        new_list_dict = []
        for operation in data:
            pattern = search
            if operation["description"]:
                dict_search = re.search(pattern, operation["description"], flags=re.IGNORECASE)
                if dict_search:
                    new_list_dict.append(operation)
                else:
                    continue
            else:
                continue
        return new_list_dict
    except Exception as ex:
        print(ex)


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь с ключами названий категорий, а значения количество операций в каждой категории."""
    try:
        new_list = []
        for operation in data:
            new_list.append(operation.get("description"))
        operation_count = Counter(item for item in new_list if item in categories)
        print(operation_count)
        return dict(operation_count)
    except Exception as ex:
        print(f"Error {ex}")


def checking_description(data: list[dict]) -> list:
    new_list = []
    for operation in data:
        new_list.append(operation.get("description"))
    return list(set(new_list))
