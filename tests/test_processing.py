from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(filter_state, filter_state_executed):
    """Тест функции отбора словарей по заданному параметру 'state'"""
    assert filter_by_state(filter_state, state="EXECUTED") == filter_state_executed


def test_filter_by_state_cancel(filter_state, filter_state_cancel):
    """Тест функции отбора словарей по заданному параметру 'state'"""
    assert filter_by_state(filter_state, state="CANCELED") == filter_state_cancel


def test_filter_by_state_(filter_state, filter_state_executed):
    """Тест функции отбора словарей по заданному параметру 'state', словари с заданным параметром отсутствуют"""
    assert filter_by_state(filter_state, state="CANC") == []


def test_sort_by_date(filter_state):
    """Тест функции сортировки по дате, в т.ч. с одинаковой датой"""
    assert sort_by_date(filter_state, reverse=True) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_rev(filter_state):
    """Тест функции сортировки по дате, в т.ч. с одинаковой датой"""
    assert sort_by_date(filter_state, reverse=False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
