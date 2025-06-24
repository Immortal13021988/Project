import os
from dotenv import load_dotenv
import requests
from typing import Dict

load_dotenv()

API_KEY = os.getenv("API_KEY")


def sum_transaction(transaction: Dict) -> float:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция была в USD
    или EUR, происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы
    операции в рубли
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])  # результат преобразуем во float
    elif transaction["operationAmount"]["currency"]["code"] != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={transaction[
            "operationAmount"]["currency"]["code"]}&amount={transaction["operationAmount"]["amount"]}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        result = response.json()
        return round(result["result"], 2)  # результат округляем до двух символов после запятой
