from unittest.mock import patch
from src.external_api import sum_transaction
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def test_sum_transaction_rub(transaction_rub):
    assert sum_transaction(transaction_rub) == 31957.58


@patch('requests.get')
def test_sum_transaction_usd(mock_get, transaction_usd):
    mock_get.return_value.json.return_value = {"result": 645372.41}
    assert sum_transaction(transaction_usd) == 645372.41
    mock_get.assert_called_once_with(
        'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37',
        headers={"apikey": API_KEY})
