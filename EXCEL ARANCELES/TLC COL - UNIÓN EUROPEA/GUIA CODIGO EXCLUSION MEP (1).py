import pandas as pd
datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura")
print(datos)
Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
    if tasa != "MEP (1)":
        tasa = tasa*100
        sumatoria+=tasa
promedio = sumatoria/(len(Tasas))
print(promedio)