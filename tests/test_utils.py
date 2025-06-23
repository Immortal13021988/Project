from unittest.mock import patch, mock_open
from src.utils import open_json


@patch('builtins.open', new_callable=mock_open, read_data='[1, 2, 3]')
@patch('json.load')
def test_open_json(mock_json_load, mock_open_in):
    mock_json_load.return_value = [1, 2, 3]
    result = open_json('fake_file.json')
    assert result == [1, 2, 3]
    mock_open_in.assert_called_once_with('fake_file.json', encoding="utf-8")
    mock_json_load.assert_called_once()


def test_open_json_not():
    assert open_json('not_file.json') == []
