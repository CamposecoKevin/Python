import random

opciones = ("piedra", "papel", "tijera")

escoger = input("Eliga papel, tijera, o piedra")
escoger = (escoger.lower())
if not escoger in opciones:
    print("Esa opción no es valida")

computador = random.choice(opciones)
print("Opción que elige usuario", escoger)
print("Opción que elige computadora", computador)
if escoger == computador:
    print("es un empate")
elif escoger == "piedra":
    if computador == "tijera":
        print("piedra gana tijera")
        print("Usuario gano")
    else:
        print("papel gana piedra")
        print("computadora gana")
elif escoger == "papel":
    if computador == "piedra":
        print("Papel gana piedra")
        print("usuario gano")
    else:
        print("Tijera corta papel")
        print("Gana Computadora")
elif escoger == "tijera":
    if computador == "papel":
        print("tijera corta papel")
        print("gana usuario")
    else:
        print("piedra gana tijera")
        print("gana computadora")
