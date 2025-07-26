import pandas as pd

datos = pd.read_excel("Estudiantes.xlsx")


def mostrarDatos(x):
    print(x)
mensajeParaPrueba = "PruebaFuncion"
numero = 8

mostrarDatos(mensajeParaPrueba)
mostrarDatos(numero)
mostrarDatos(datos)

def mostrarCuadrado(numero):
    print(numero*numero)

mostrarCuadrado(3)
mostrarCuadrado(8)
mostrarCuadrado(12)

def ACadaNumeroQueIngreseResteDos (numero):
    print(numero-2)

ACadaNumeroQueIngreseResteDos (7)
ACadaNumeroQueIngreseResteDos (65)
ACadaNumeroQueIngreseResteDos (74)



#print(datos)

def funcionHallarEstadisticasDeEdad(datosLeidosExcel):
    promedio = datosLeidosExcel['EDAD'].mean()
    desviacion = datosLeidosExcel['EDAD'].std()
    mediana = datosLeidosExcel['EDAD'].median()
    print("El promedio es: ",promedio)
    print("La desviacion estandar es: ",desviacion)
    print("La mediana es: ",mediana)


estadisticas = datos.describe()

print(estadisticas)

print("Explicacion final")
funcionHallarEstadisticasDeEdad(datos)
