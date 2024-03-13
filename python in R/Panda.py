import pandas as pd
import openpyxl as px
import matplotlib.pyplot as plt

data1 = pd.read_excel('C:/Users/Kevin Camposeco/Downloads/Reporte Asistencias por Organización.xlsx')

## para que muestre todas las columans de los dotos
pd.options.display.max_columns = None

data1.head(2)


data1.info()
View(data1)

data1.dropna(inplace = True)


#duplicados para ver is hay

data1["Departamento"].duplicated()


#para eliminar duplicados

depto= data1["Departamento"].drop_duplicates()
siglas_organizacion= data1["Siglas"].drop_duplicates()


#Convertir en data frame
depto=depto.to_frame()
siglas_organizacion=siglas_organizacion.to_frame()

data1[[5,6]]



## gráficos

data1["No. De Asistencias"].plot()
data1["No. De Asociados"].plot()

plt.show()


#scaterplot usualmente se usa para correlaciones.
data1.plot(kind = 'scatter', x = 'No. De Asistencias', y = 'No. De Asociados')
plt.show()








