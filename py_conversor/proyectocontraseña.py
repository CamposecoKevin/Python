import random

def generar_contrasena():
    mayusculas= ['A','B','C','D','F','G']
    minuscula= ['a','b','c','d','f','g']
    simbolos= ['!',',','#','&','/',')']
    numeros= ['1','2','3','4','5','6']

    caracteres =mayusculas+minuscula+simbolos+numeros

    contrasena = []

    for i in range (15):
        caracter_random= random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena= ''.join(contrasena)
    return contrasena



def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es : '+ contrasena)


if __name__=='__main__':
    run()