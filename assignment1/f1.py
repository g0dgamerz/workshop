def maax(a, b, c):
    if (a >= b) and (a >= c):
        large = a
    elif (b >= a) and (b >= c):
        large = b
    else:
        large = c

    return large


print('maximum number is=', maax(1, 2, 3))
