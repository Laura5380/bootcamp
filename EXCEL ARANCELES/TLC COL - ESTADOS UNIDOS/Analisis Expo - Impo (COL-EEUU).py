import pandas as pd

class seccion1:
    datos = pd.read_excel("TLC COLOMBIA - ESTADOS UNIDOS.xlsx", sheet_name="Industrial EX")
    Tasas = datos['Tasa Base']
    sumatoria = 0
    for tasa in Tasas:
            if isinstance(tasa, (int, float)):
                sumatoria+=tasa
                promedio = sumatoria/(len(Tasas))

    print("El promedio arancelario para productos industriales de COL_EEUU es :",promedio)

class seccion2:
    datos = pd.read_excel("TLC COLOMBIA - ESTADOS UNIDOS.xlsx", sheet_name="Agricultura EX")

    Tasas = datos['Tasa Base']
    sumatoria = 0
    for tasa in Tasas:
            if isinstance(tasa, (int, float)):
                sumatoria+=tasa
                promedio = sumatoria/(len(Tasas))

    print("El promedio arancelario para productos agricolas de COL_EEUU es :",promedio)

class seccion3:
    datos = pd.read_excel("TLC COLOMBIA - ESTADOS UNIDOS.xlsx", sheet_name="Agricultura IM")

    Tasas = datos['Tasa Base']
    sumatoria = 0
    for tasa in Tasas:
            if isinstance(tasa, (int, float)):
                sumatoria+=tasa
    promedio = sumatoria/(len(Tasas))

    print("El promedio arancelario para productos agricolas de EEUU_COL es : ", promedio)

class seccion4:
    datos = pd.read_excel("TLC COLOMBIA - ESTADOS UNIDOS.xlsx", sheet_name="Industrial IM")

    Tasas = datos['Tasa Base']
    sumatoria=0
    for tasa in Tasas:
        if isinstance(tasa, (int, float)):
         sumatoria+=tasa

    promedio = sumatoria/(len(Tasas))
    print("El promedio arancelario para productos industriales de EEUU_COL es : ", promedio)