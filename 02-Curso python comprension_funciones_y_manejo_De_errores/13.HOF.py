def increment(x):
    return x+1


def high_ord_func(x, func):
    return x + func(x)


restult = high_ord_func(2, increment)
print(restult)
