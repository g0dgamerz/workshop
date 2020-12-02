def decorate_me(func):
    def inner_func():
        print("It is now decorated")
        func()
        print("ths")
    return inner_func


@decorate_me
def ordinary():
    print('ordinary')


# decorated = decorate_me(ordinary)
# decorated()
#ordinary = decorate_me(ordinary)
ordinary()
