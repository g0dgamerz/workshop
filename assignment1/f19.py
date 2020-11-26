# ​ Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce


def fib_series(n): return reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])


print("Fibonacci series upto 3:")
print(fib_series(3))
