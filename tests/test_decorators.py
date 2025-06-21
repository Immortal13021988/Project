from src.decorators import log


def test_log(capsys):
    func_example(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "func_example ok\n"


def test_log_err(capsys):
    func_example(1, (1, 2))
    captured = capsys.readouterr()
    assert captured.out == "func_example error: TypeError, Inputs: (1, (1, 2)), {}\n"


@log()
def func_example(x, y):
    return x + y
