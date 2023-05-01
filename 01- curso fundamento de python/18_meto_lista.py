# crud : create, read, update, delete.

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(number[:4])


# agregar nuevo element
number.append(11)
print(number)

# insertar de una posición especificada.

number.insert(0, "Aqui empeiza")
print(number)

# unir listas

task = ["toodo 1", "tood 2"]

new_list = number+task
print(new_list)

# encontrar la posicón
index = new_list.index("toodo 1")
print(index)

new_list[index] = "Toodo_1"
print(new_list)

# remover elementos
new_list.remove("Toodo_1")
print(new_list)

# eliminar el ultimo elementi
new_list.pop()
# eliminar la posición que se quiere
new_list.pop(0)

print(new_list)


# reverse
new_list.reverse()
print(new_list)

# ordern lista, que esta desordenada
number_2 = [1, 11, 7, 6, 4]
number_2.sort()
print(number_2)
