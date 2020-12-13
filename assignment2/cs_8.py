# Write a function, is_prime, that takes an integer and returns True if the
# number is prime and False if the number is not prime.
def is_prime(num):
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                return False

            else:
                print(num, "is a prime number")
                return True

    # if input number is less than or equal to 1 it is not prime
    else:
        print(num, "is not a prime number")
        return False


n = int(input("enter any number to check wheater it is prime or not"))
is_prime(n)
