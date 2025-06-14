from src.generators import filter_by_currency, transaction_descriptions

def test_filter_by_currency():
    filter_cur = filter_by_currency()
    assert  next(filter_cur) == filter_by_currency_1