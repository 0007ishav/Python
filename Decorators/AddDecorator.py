def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        print(f"Arguments are :  {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(3, 4))