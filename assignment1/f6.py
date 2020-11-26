# Write a Python function to check whether a number is in a given range.
def test_range(n, a, b):
    if n in range(3, 9):
        print(" %s is in the range" % str(n))
    else:
        print("The number is outside the given range.")


n = input("enter the number you what to find range")
a = input("enter 1st number of range ")
b = input("enter 2nd number of range")
test_range(n, a, b)
