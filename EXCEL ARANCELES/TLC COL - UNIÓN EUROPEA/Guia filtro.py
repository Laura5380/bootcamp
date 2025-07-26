import pandas as pd
datos = pd.read_excel("TLC COL - UNIÓN EUROPEA.xlsx", sheet_name="Agricultura EX")
print(datos)

promedio = datos['Tasa Base'].mean()
print("El promedio es: ",promedio)

