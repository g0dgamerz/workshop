# Write a Python function to multiply all the numbers in a list.
# Sample List ​: (8, 2, 3, -1, 7)
# Expected Output​ : -336
def mul(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(mul([8, 2, 3, -1, 7]))
