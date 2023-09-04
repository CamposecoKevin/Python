def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum


result = sum_with_range(10, 20)
print(result)

sum_with_range(23, 100)
