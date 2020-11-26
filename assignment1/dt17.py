# Write a Python program to multiplies all the items in a list
def mul_list(items):
    mul_numbers = 1
    for x in items:
        mul_numbers *= x
    return mul_numbers


print(mul_list([1, 2, 3]))
