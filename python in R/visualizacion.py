import pandas as pd
import openpyxl as px
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sb
import numpy as np


use_virtualenv("py32", required = True)

x1 = np.linspace(0,5,11)
y1 = x**2

#evitar que se coloque encima de los graficos
plt.clf()

##plt.plot(x,y, 'rs-')
plot1=plt.plot(x1,y1, 'rD:')

plot2=plt.plot(x1,y1, 'yX:')

plt.show(plot1)

plt.show(plot2)

plt.boxplot(x1)
plt.show()


np.random.seed(0)



# subplot


x = np.linspace(0,5,11)
y = x**2

#usando subplot, para mostrar varias graficas en una sola imagen, en este
#caso, 1 fila, y 2 columnas
plt.subplot(1,2,1) ##para agregar la primera gráfica
plt.plot(x,y, 'r--')      #grafica 1
plt.subplot(1,2,2) ## para agregar la segunda gráfica
plt.hist(y, color = "C1")        ## grafica 2

#mostrar grafica
plt.clf()
plt.show()


data1 = pd.read_excel('C:/Users/Kevin Camposeco/Downloads/Reporte Asistencias por Organización.xlsx')

data1.info()
View(data1)

plt.hist()

plt.ba

plt.clf()
plt.figure(figsize =(2,10), dpi = 60)
plt.barh(data1["Siglas"],data1["No. De Asociados"]>200)
plt.show()


# metodo orientado en objetos
plt.clf()
x=data1["Siglas"]
y=data1["No. De Asociados"]
fig= plt.figure(figsize =(2,5))
axes = fig.add_axes([0.2,.1,0.4,1])
axes.barh(x,y)
fig.tight_layout()
plt.show()



plt.clf()
x=data1["Siglas"]
y=data1["No. De Asociados"]
fig= plt.figure()
axes = fig.add_axes([0.25,.1,.6,0.8])
axes.set_title("Organización y asociados")
axes.set_xlabel("Asociados")
axes.set_ylabel("Organización")
axes.legend()
axes.barh(x,y)
plt.show()


#subplots




