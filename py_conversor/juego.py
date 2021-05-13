import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un número más grande')
        else:
            print('busca un número more small')
        numero_elegido = int(input('elige otro número: '))
        print('ganaste')


if __name__ == "__main__":
    run()