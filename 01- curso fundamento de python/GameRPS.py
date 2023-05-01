import random

opciones = ("piedra", "papel", "tijera")
computador_wins = 0
usuaario_win = 0
rouds = 1


while True:
    print('*' * 10)
    print("Round", rouds)
    print('*' * 10)

    print("Cuanto va computadora", computador_wins)
    print("cuanto va usuario", usuaario_win)

    escoger = input("Eliga papel, tijera, o piedra")
    escoger = (escoger.lower())
    if not escoger in opciones:
        print("Esa opción no es valida")
        continue
    rouds += 1

    computador = random.choice(opciones)
    print("Opción que elige usuario", escoger)
    print("Opción que elige computadora", computador)
    if escoger == computador:
        print("es un empate")
    elif escoger == "piedra":
        if computador == "tijera":
            print("piedra gana tijera")
            print("Usuario gano")
            usuaario_win += 1
        else:
            print("papel gana piedra")
            print("computadora gana")
            computador_wins += 1
    elif escoger == "papel":
        if computador == "piedra":
            print("Papel gana piedra")
            print("usuario gano")
            usuaario_win += 1
        else:
            print("Tijera corta papel")
            print("Gana Computadora")
            computador_wins += 1
    elif escoger == "tijera":
        if computador == "papel":
            print("tijera corta papel")
            print("gana usuario")
            usuaario_win += 1
        else:
            print("piedra gana tijera")
            print("gana computadora")
            computador_wins += 1
    if computador_wins == 2:
        print("El cumputador gano")
        break
    if usuaario_win == 2:
        print("El usuario gana")
        break

    rouds += 1
