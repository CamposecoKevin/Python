import pandas as pd
import openpyxl as px
import matplotlib.pyplot as plt
import numpy as np
import psycopg2 as psp

ProductoresR1 = pd.read_excel("G:/Mi unidad/1. Proinnova (Agricultura)/Proinnova II/05.Productores/Productores R1/ProductoresR1.xlsx")

## para que muestre todas las columans de los dotos
pd.options.display.max_columns = None

print(ProductoresR1)
#Muestra un resumen de lo que contiene el data frame y de que tipo son.
ProductoresR1.info()

#convertir en Data Frame
ProductoresR1DF= pd.DataFrame(ProductoresR1)

## para visualizar las primeras 2 filas
ProductoresR1DF.head(2)
##para visualizar las últimas 2 filas
ProductoresR1DF.tail(2)

##para visualizar los datos
print(ProductoresR1)


print(pd.__version__)

# 01 Data Frame

#Muestra el número de registro de 0 a ...
print(ProductoresR1DF.loc[10])

#Muestra el registro 0, 1 y las columnas que tiene
print(ProductoresR1DF.loc[[0, 1]])


print(ProductoresR1DF.loc["Adolfo Torres Ixcoy"])


#02 Data Cleaning, 

#CELDAS VACIAS

#fist step, view the data, can you view what kind of data you have.
ProductoresR1DF.info()


#Eliminar las filas con NA,  y deja las que si tiene.
New_ProductoresR1DF = ProductoresR1DF.dropna()

#Nuevo conjunto de datos in NA
New_ProductoresR1DF.info()

print(New_ProductoresR1DF.to_string)

#Reemplazar el null por un valor, en este caso valor 0
ProductoresR1DF.fillna(0, inplace = True)


#para cambiar los na, puedes usar la media, promedio, o moda.
#esto craendo una medida

#promedio
x=ProductoresR1["Hectareas"].mean()
#Media
x1=ProductoresR1["Hectareas"].median()
#Moda
x2=ProductoresR1["Hectareas"].mode()[0]

# o
ProductoresR1.fillna(ProductoresR1.mean())

#para hacer el cambio ya solo psar la variable, el INPLACE = true
#significa que los cambios a realizar se van a mantener en el conjunto de datos
ProductoresR1DF["Hectareas"].fillna(x1, inplace = True)

View(ProductoresR1DF)


# 03 mal formato 

#para las fechas
df['Date'] = pd.to_datetime(df['Date'])

# incertar valores en filas especificas
df.loc[7, 'Duration'] = 45

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


ProductoresR1.info()

#Eliminar columnas de una base de datos
ProductoresR1.drop("Entidad", axis = 1, inplace = True)
#Eliminar varias columnas
ProductoresR1.drop(["Genero", "Edad"], axis = 1, inplace = True)


#Eliminar filas
ProductoresR1.drop(0, axis = 0, inplace = True)
#borrar una lista
ProductoresR1.drop([0,1,2,3], axis = 1, inplace = True)



# agregar columnas

ProductoresR1['Null'] = np.nan
ProductoresR1.info()

# cantiad de na en una columna
ProductoresR1.isnull().sum()
#llenar los na
ProductoresR1["Hectareas"].fillna(ProductoresR1["Hectareas"].mean(), inplace = True)
ProductoresR1.isnull().sum()


# filtrar por condiciones
ha_mayor_20= ProductoresR1["Hectareas"]>20

ha_mayor_20=ProductoresR1[ProductoresR1["Hectareas"]>20]



# funciones principales

.info()
.head()
.tail()
.describe()
.memory_usage(deep=True)
.value_counts()
.drop_duplicates(keep ='last')
.sort_values("Hectareas", ascending= False)


ProductoresR1["Hectareas"].describe()

ProductoresR1["Tecnico"].drop_duplicates(keep="last")




# groupby

ProductoresR1.groupby("Municipio").count()
ProductoresR1.groupby(["Departamento", "Municipio"]).count()

# de uno en especifico

ProductoresR1.groupby("Municipio").coun().loc['Chajul']


#metricas especificas
ProductoresR1.groupby("Municipio").agg('min', 'max')

#metrica especifa de columna a estudiar
ProductoresR1.groupby('Municipio').agg({'Hectareas':['min','max'],"Productor":'count'})


#Unir data frames

merge
join
concat

pd.concat(['dataframe1','Dataframe2'], ignore_index= True)
pd.concat(['dataframe1','Dataframe2'],axis = 1)

#Combinar con llaves iguales en cada dataframe
dataframe2.merge(dataframe2 on = "Lllave")

#combiar pero con nombres de llaves diferentes
dataframe2.merge(dataframe2 left_on = "Lllave", right_on = "Llave 2")


# al utilizar how, nos indica que data frame priorizara, esta left o right, inner
dataframe2.merge(dataframe2 left_on = "Lllave", right_on = "Llave 2", how= 'left')



#JOIN A TRAVES DE INDEX MACH: join, inner, left, outer, 
 
dataframe1.join(dataframe2, how = 'join')


#usando pivot_table

newdata= ProductoresR1.pivot_table(index = 'Tecnico', columns = "Departamento", values = "ID_Productor"
, aggfunc = "count")


#MELT 
df_books[['Name','Genre']].head(5).melt()




#apply



















