number = [1, 2, 3, 4]
number_v2 = []

for i in number:
    number_v2.append(i*2)


number_v3 = list(map(lambda i: i*2, number))

print(number)
print(number_v2)
print(number_v3)
