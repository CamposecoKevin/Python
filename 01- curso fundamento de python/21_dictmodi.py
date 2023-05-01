persona = {
    "Nombre": "Kevin",
    "Apellido": "Camposeco",
    "Año": "27",
    "lenguaje": ["Python", "R"]
}

print(persona)
# modificando variables guardadas anteriormente

persona["Nombre"] = "Rubeli"
persona["lenguaje"].append("js")
print(persona)

# eliminar
del persona["Apellido"]
print(persona)


# obtener los items
print("items")
print(persona.items())


print("Keys")
print(persona.keys())

print("Values")
print(persona.values())


person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
del person["age"]

print(list(person.keys()))
print(list(person.values()))
