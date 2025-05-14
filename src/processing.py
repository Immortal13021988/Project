from typing import List, Dict, Any


def filter_by_state(dict_filter: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in dict_filter if item.get("state") == state]


def sort_by_date(sort_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(sort_data, key=lambda x: str(x.get("date")), reverse=reverse)
