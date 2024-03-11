import pandas as pd
import openpyxl as px

data1 = pd.read_excel('C:/Users/Kevin Camposeco/Downloads/Reporte Asistencias por Organización.xlsx')

## para que muestre todas las columans de los dotos
pd.options.display.max_columns = None

data1.head(2)


print(data1)
