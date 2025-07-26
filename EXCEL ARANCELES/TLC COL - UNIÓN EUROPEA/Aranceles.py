import pandas as pd

datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Industrial EX")
print(datos)

Tasas = datos['Tasa Base']
sumatoria = 0
for tasa in Tasas:
    if tasa != "MEP (1)":
        tasa = tasa*100
        sumatoria+=tasa

promedio = datos['Tasa Base'].mean()
desviacion = datos['Tasa Base'].std()
mediana = datos['Tasa Base'].median()


print("El promedio es: ",promedio)
print("La desviacion estandar es: ",desviacion)
print("La mediana es: ",mediana)




