from functools import wraps


def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""
    def my_decorator(function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            name = function.__name__
            try:
                res = function(*args, **kwargs)
                log_message = f"{name} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return res
            except Exception as e:
                error = e.__class__.__name__
                log_message = f"{name} error: {error}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                raise e

        return wrapped

    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
