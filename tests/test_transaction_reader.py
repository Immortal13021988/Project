from unittest.mock import patch
from src.transaction_reader import open_xlsx, open_csv


@patch('pandas.read_excel')
def test_open_xlsx(mock_pd):
    mock_pd.return_value.to_dict.return_value = [{1: 1}, {1: 1}]
    result = open_xlsx('fake_file.xlsx')
    assert result == [{1: 1}, {1: 1}]
    mock_pd.assert_called_once_with('fake_file.xlsx')


def test_open_xlsx_not():
    assert open_xlsx('fake_file.xlsx') == []


@patch('pandas.read_csv')
def test_open_csv(mock_pd):
    mock_pd.return_value.to_dict.return_value = [{1: 1}, {1: 1}]
    result = open_csv('fake_file.csv')
    assert result == [{1: 1}, {1: 1}]
    mock_pd.assert_called_once_with('fake_file.csv', delimiter=";")


def test_open_csv_not():
    assert open_csv('fake_file.csv') == []
