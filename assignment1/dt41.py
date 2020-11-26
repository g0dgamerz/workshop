# .​ Write a Python program to convert a tuple to a string.
def convertTuple(tup):
    str = ''.join(tup)
    return str


# Driver code
tuple = ('i', 'n', 's', 'i', 'g', 'h', 't', ' ',
         'w', 'o', 'r', 'k', 's', 'h', 'o', 'p')
str = convertTuple(tuple)
print(str)
