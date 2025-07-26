import pandas as pd

datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura IM")

Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
           if isinstance(tasa, (int, float)):
            sumatoria+=tasa
            promedio = sumatoria/(len(Tasas))

print("El promedio arancelario para productos agricolas de UE_COL es : ",promedio)

"""
datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura IM")
Tasas = datos['Tasa Base']

for tasa in Tasas:
    if tasa == (tasa, (int, float)):
        tasa = tasa*100
        sumatoria += tasa
promedio = sumatoria/(len(Tasas))

print("valio",promedio)
"""

datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Industrial IM")
Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
           if isinstance(tasa, (int, float)):
            sumatoria+=tasa
            promedio = sumatoria/(len(Tasas))

print("El promedio arancelario para productos industriales de UE_COL es : ", promedio)