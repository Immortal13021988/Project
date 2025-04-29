def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    mask_card_number = f'{"".join(card_number[:4])} {"".join(card_number[4:6])}** **** {"".join(card_number[12:])}'
    return mask_card_number


def get_mask_account(score: int) -> str:
    """Функция маскировки номера банковского счета"""
    score = str(score)
    mask_card_number = f'**{"".join(score[-4:])}'
    return mask_card_number
