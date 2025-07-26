import pandas as pd

datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura IM")

Tasas = datos['Tasa Base']
sumatoria = 0
numeros = [Tasas for x in datos 
           if isinstance(x, (int, float))]

if numeros:
    promedio= sum(numeros) / len(numeros)
    print("El promedio es :",promedio)