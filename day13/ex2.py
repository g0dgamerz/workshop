def uppercase_decorator(func):
    def wrapper(string_arg):
        print("Shouts")
        return func(string_arg).upper()
    return wrapper


@uppercase_decorator
def shout(string_arg):
    return string_arg


# shout = uppercase_decorator(shout)
# print(shout("Python is fun"))

print(shout("python is ffffffuuunnn"))
