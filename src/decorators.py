from functools import wraps
from collections.abc import Callable
from typing import Any


def log(filename: str | None = None) -> Callable[..., Any]:
    """Декоратор, который автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""

    def my_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
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
