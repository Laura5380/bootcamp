import pandas as pd
datosIn = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Industrial EX")
##print(datosIn)

Tasas = datosIn['Tasa Base']
sumatoria = 0
for tasa in Tasas:
    if tasa != "MEP (1)":
        tasa = tasa*100
        sumatoria+=tasa
promedio = sumatoria/(len(Tasas))
print("El promedio arancelario para productos industriales de COL_EU es :",promedio)

datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura EX")
##print(datos)

Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
    if tasa != "MEP (1)":
        tasa = tasa*100
        sumatoria+=tasa
promedio = sumatoria/(len(Tasas))
print("El promedio arancelario para productos agricolas de COL_EU es :",promedio)

datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura IM")

Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
           if isinstance(tasa, (int, float)):
            sumatoria+=tasa
            promedio = sumatoria/(len(Tasas))

print("El promedio arancelario para productos agricolas de UE_COL es : ",promedio)


datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Industrial IM")
Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
           if isinstance(tasa, (int, float)):
            sumatoria+=tasa
            promedio = sumatoria/(len(Tasas))

print("El promedio arancelario para productos industriales de UE_COL es : ", promedio)