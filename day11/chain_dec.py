def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        print('shell shouts:')
        return func(*args, **kwargs).upper()
    return wrapper


def add_info(func):
    def wrapper(*args, **kwargs):
        # this prints the information below
        print("(on the top of it's lungs)")
        return func(*args, **kwargs)
    return wrapper


@uppercase_decorator
@add_info
def shout(string):
    return string


print(shout("python is fun"))
