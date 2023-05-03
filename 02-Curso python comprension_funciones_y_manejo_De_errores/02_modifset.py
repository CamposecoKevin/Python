set_contries = {"Guatemala", "Salvador", "Honduras"}
print(type(set_contries))
print(set_contries)


# tamaño
size = len(set_contries)
print(size)

# que hay dentro
print("Guatemala" in set_contries)


# add
set_contries.add("Costa Rica")
print(set_contries)


# actualizar
set_contries.update({"Guatemala", "Quetzaltenango"})
print(set_contries)

# remove
set_contries.remove("Quetzaltenango")
set_contries.discard("Quetzaltenango")
print(set_contries)

# Eliminar todo el conjunto
set_contries.clear()
print(set_contries)
