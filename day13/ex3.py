def general_decorator(func):
    def inner(*args, **kwargs):
        print('Dynamic Arguments')
        return func(*args, **kwargs)
    return inner


@general_decorator
def add(a, b):
    return a+b


print(add(2, 3))
