from typing import Any


def filter_by_currency(transactions: list, name: str = "USD") -> Any:
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == name:
            yield item


def transaction_descriptions(transactions: list) -> Any:
    for item in transactions:
        yield item["description"]
