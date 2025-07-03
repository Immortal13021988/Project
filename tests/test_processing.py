from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations, \
    checking_description


def test_filter_by_state_executed(filter_state, filter_state_executed):
    """Тест функции отбора словарей по заданному параметру 'state'"""
    assert filter_by_state(filter_state, state="EXECUTED") == filter_state_executed


def test_filter_by_state_cancel(filter_state, filter_state_cancel):
    """Тест функции отбора словарей по заданному параметру 'state'"""
    assert filter_by_state(filter_state, state="CANCELED") == filter_state_cancel


def test_filter_by_state_(filter_state):
    """Тест функции отбора словарей по заданному параметру 'state', словари с заданным параметром отсутствуют"""
    assert filter_by_state(filter_state, state="CANCEL") == []


def test_sort_by_date(filter_state):
    """Тест функции сортировки по дате, в т.ч. с одинаковой датой"""
    assert sort_by_date(filter_state, reverse=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_rev(filter_state):
    """Тест функции сортировки по дате, в т.ч. с одинаковой датой"""
    assert sort_by_date(filter_state, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_process_bank_search_1(transactions_list, transactions_list_1):
    """Тест функции поиска транзакций по описанию"""
    search = 'орг'
    assert process_bank_search(transactions_list, search) == transactions_list_1


def test_process_bank_search_2(transactions_list, transactions_list_2):
    """Тест функции поиска транзакций по описанию"""
    search = 'карты'
    assert process_bank_search(transactions_list, search) == transactions_list_2


def test_process_bank_search_3(transactions_list, transactions_list_3):
    """Тест функции поиска транзакций по описанию"""
    search = 'счет'
    assert process_bank_search(transactions_list, search) == transactions_list_3


def test_process_bank_search_not(transactions_list):
    """Тест функции поиска транзакций по несуществующему описанию"""
    search = 'карат'
    assert process_bank_search(transactions_list, search) == []


def test_process_bank_search_not_2(transactions_list_not):
    """Тест функции поиска транзакций по несуществующему описанию"""
    search = 'карат'
    assert process_bank_search(transactions_list_not, search) == []


def test_process_bank_search_ex():
    """Тест функции поиска транзакций с ошибкой"""
    search = 'карат'
    assert process_bank_search([{1: 2}, {3: 4}, {5: 6}], search) == []


def test_process_bank_operations(transactions_list, categories, categories_result):
    """Тест функции подсчета транзакций по описанию"""
    assert process_bank_operations(transactions_list, categories) == categories_result


def test_process_bank_operations_not(categories):
    """Тест функции подсчета транзакций по описанию, с ошибочным списком транзакций"""
    assert process_bank_operations([{1: 2}, {3: 4}, {5: 6}], categories) == {}


def test_checking_description(transactions_list, categories_result_check):
    """Тест функции выявления всех возможных описаний транзакций в списках транзакций"""
    assert checking_description(transactions_list) == categories_result_check
