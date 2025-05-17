from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция определяет входной аргумент и маскирует его, в зависимости от данных"""
    account_card_split = account_card.split()
    if len(account_card_split) > 1:
        if "Счет" in account_card_split:
            if get_mask_account(account_card_split[-1]) != "Номер счета введен неверно":
                return f"Счет {get_mask_account(account_card_split[-1])}"
            return "Номер счета введен неверно"
        elif account_card_split[1] == account_card_split[-1]:
            if get_mask_card_number(account_card_split[-1]) != "Номер карты введен неверно":
                return f'{" ".join(account_card_split[:1])} {get_mask_card_number(account_card_split[-1])}'
            return "Номер карты введен неверно"
        else:
            if get_mask_card_number(account_card_split[-1]) != "Номер карты введен неверно":
                return f'{" ".join(account_card_split[:2])} {get_mask_card_number(account_card_split[-1])}'
            return "Номер карты введен неверно"
    return "Номер введен неверно"


def get_date(date_time: str) -> str:
    """Функция преобразует дату"""
    if "T" in date_time:
        split_date_time = date_time.split("T")
        date = split_date_time[0]
        date_split = date.split("-")
        if len(date_split) > 2 and len(date_split[0]) == 4 and len(date_split[1]) == 2 and len(date_split[2]) == 2:
            return f"{date_split[1]}.{date_split[2]}.{date_split[0]}"
        return "Введен неверный формат даты"
    return "Введен неверный формат даты"

print(get_date("202-4-03-11T02:26:18-671407"))