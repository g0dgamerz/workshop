#  Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    if y == 0:
        print("Divisior can't be zero")
    return x / y


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operators = str(input("Enter + or - or * or / as per your requirements"))
if operators == '+':
    print(add(num1, num2))
elif operators == '-':
    print(subtract(num1, num2))
elif operators == '*':
    print(multiply(num1, num2))
elif operators == '/':
    if num2 == 0:
        raise Exception("Demonenator or divisor can't be zero")
    print(divide(num1, num2))
