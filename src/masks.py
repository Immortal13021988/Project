import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Функция маскировки номера банковской карты запущена")
    card_number = str(card_number)
    logger.info("Проверяем корректность номера банковской карты")
    if len(card_number) == 16 and card_number.isdigit():
        mask_card_number = f'{"".join(card_number[:4])} {"".join(card_number[4:6])}** **** {"".join(card_number[12:])}'
        logger.info("Маскировки номера банковской карты выполнена")
        return mask_card_number
    logger.error("Провалена проверка корректности номера банковской карты")
    return "Номер карты введен неверно"


def get_mask_account(score: Union[str, int]) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info("Функция маскировки номера счета запущена")
    score = str(score)
    logger.info("Проверяем корректность номера счета")
    if len(score) == 20 and score.isdigit():
        mask_card_number = f'**{"".join(score[-4:])}'
        logger.info("Маскировки номера счета выполнена")
        return mask_card_number
    logger.error("Провалена проверка корректности номера счета")
    return "Номер счета введен неверно"
