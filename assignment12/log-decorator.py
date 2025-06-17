import logging
from functools import wraps

# ---------- one-time logger setup ----------
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# ---------- decorator ----------
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(
            "function: %s | positional: %s | keywords: %s | return: %s",
            func.__name__,
            list(args) if args else "none",
            kwargs if kwargs else "none",
            result
        )
        return result
    return wrapper

# ---------- three test functions ----------
@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def all_positional(*args):
    return True

@logger_decorator
def all_keyword(**kwargs):
    return logger_decorator   # arbitrary return to show logging

# ---------- mainline ----------
if __name__ == "__main__":
    hello_world()
    all_positional(1, 2, 3, "abc")
    all_keyword(name="Nya", age=35)
    print("Check decorator.log for entries.")