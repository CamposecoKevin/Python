menu = """

BIENVENIDOS A MI CONVERTIDOR DE MONEDAS
1- PESOS COLOMBIANOS
2- PESOS ARGENTINOS
3- PESOS MEXICANOS

ELIGE UNA OPCIÓN:

"""
def conversor (tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos"  +tipo_pesos+  " tienes?")
    pesos= float(pesos)
    dolares= pesos/valor_dolar
    dolares=round(dolares,2)
    dolares =str(dolares)
    print("tienes $"+ dolares + "dolares")    


opcion = int(input(menu))
if opcion ==1:
    conversor("Colombianos", 3875)

elif opcion ==2:
    conversor("Argentinos", 65)
elif opcion ==3:
    conversor("mexicanos", 24)
else:
    print('Seleccione una opcion que se encuentre en el menu')


