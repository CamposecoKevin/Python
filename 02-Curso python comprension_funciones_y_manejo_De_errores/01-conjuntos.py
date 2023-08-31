# conjuntos
set_contries = {"Guatemala", "Salvador", "Honduras"}
print(type(set_contries))
print(set_contries)

# conjuntos solo cuenta unicos
#usar set con función de conjunto

numbers = [1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9]
set_number = set(numbers)
print(set_number)

# convertir el set, en lista
unique_numerbers = list(set_number)
print(unique_numerbers)

print("El numero en la posición 4 de la lista es ", unique_numerbers[3])
