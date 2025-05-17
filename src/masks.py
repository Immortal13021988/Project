from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if len(card_number) == 16 and card_number.isdigit():
        mask_card_number = f'{"".join(card_number[:4])} {"".join(card_number[4:6])}** **** {"".join(card_number[12:])}'
        return mask_card_number
    return "Номер карты введен неверно"


def get_mask_account(score: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    score = str(score)
    if len(score) == 20 and score.isdigit():
        mask_card_number = f'**{"".join(score[-4:])}'
        return mask_card_number
    return "Номер счета введен неверно"
