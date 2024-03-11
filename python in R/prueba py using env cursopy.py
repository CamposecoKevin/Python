import matplotlib.pyplot as plt
import numpy as np
eje_X1 =['Py','R','Node']

eje_y2 = [50,20,35]

grap_lenguajeprogrami= plt.bar(eje_X1, eje_y2)

plt.ylabel("Cantidad de ususario")
plt.xlabel("Lenguajes de programación")
plt.title("Usuaarios de lenguaje de programación")

#para mostrar la gráfica
plt.show(grap_lenguajeprogrami)


#para identificar el tamaño
plt.figure()


