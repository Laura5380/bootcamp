import pandas as pd

datos = pd.read_excel("TLC COLOMBIA - ESTADOS UNIDOS.xlsx", sheet_name="Industrial IM")

Tasas = datos['Tasa Base']
sumatoria=0
for tasa in Tasas:
    if isinstance(tasa, (int, float)):
       sumatoria+=tasa

promedio = sumatoria/(len(Tasas))
print(promedio)
