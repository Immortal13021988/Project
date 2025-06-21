def log(filename=None):
    """Декоратор логирования функции"""
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                success_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                    return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}, Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a', encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)

        return inner

    return wrapper
