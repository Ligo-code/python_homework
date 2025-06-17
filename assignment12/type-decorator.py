from functools import wraps

def type_converter(type_of_output):
    """Decorator factory – converts return value to given type."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5            # becomes "5"

@type_converter(int)
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)          # --> str
    try:
        y = return_string()          # raises ValueError
    except ValueError:
        print("can't convert that string to an integer!")