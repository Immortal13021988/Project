from time import time


def log(filename = None):
    def wrapper (func):
        def inner(*args, **kwargs):
            print("Начало работы")
            result = func(*args, **kwargs)
            print(f"Результат", result)
            print("Конец работы")
            try:
                result = func(*args, **kwargs)
                success_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}, args: {args}, kwargs: {kwargs}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise
            return result
        return inner
    return wrapper



