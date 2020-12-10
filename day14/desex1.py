class DescrAttribute:
    def __get__(self, obj, type=None):
        print("accessing the attribute to get the value")
        print("__get__ is called")
        return 100

    def __set__(self, obj, value):
        print("accessing the attribute to set the value")
        print("__set__ is called")
        raise AttributeError("cannot change the value")


class MyClass:
    attr1 = DescrAttribute()


obj = MyClass()
print(obj.attr1)
# output
# accessing the attribute to get the value
# __get__ is called
# 100

obj.attr1 = 10
