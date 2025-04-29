from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция определяет входной аргумент и маскирует его, в зависимости от данных"""
    account_card_split = account_card.split()
    if "Счет" in account_card_split:
        return f"Счет {get_mask_account(account_card_split[-1])}"
    elif account_card_split[1] == account_card_split[-1]:
        return f'{" ".join(account_card_split[:1])} {get_mask_card_number(account_card_split[-1])}'
    else:
        return f'{" ".join(account_card_split[:2])} {get_mask_card_number(account_card_split[-1])}'


def get_date(date_time: str) -> str:
    """Функция преобразует дату"""
    split_date_time = date_time.split("T")
    date = split_date_time[0]
    date_split = date.split("-")
    return f"{date_split[1]}.{date_split[2]}.{date_split[0]}"
