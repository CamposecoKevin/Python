#working in env called pykevin
reticulate::conda_python('pykevin')

#creat enviroment py

reticulate::repl_python()

#import package to work
import pandas as pd

#data frame
df_reporteT1=pd.read_excel('C:/Users/Kevin/Downloads/Reportes Técnicos.xlsx')

df_reporteT1.head (2)
