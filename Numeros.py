import pandas as pd

numeros= [1,2,3,4,5]

print(numeros)

def multiplicarNumeroPorDos(ListaNumeros):
    for numero in ListaNumeros:
        print(numero*2)

#multiplicarNumeroPorDos(numeros)

diasDeLaSemana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

def leerDiasDeLaSemana(semana):
    for dia in semana:
        if dia =="Sabado":
           print("Es fin de semana, el dia actual es",dia)
        elif dia =="Domingo":
           print("Es fin de semana, el dia actual es",dia)
        else:
           print("El dia actial es",dia)

#leerDiasDeLaSemana(diasDeLaSemana)

while True:
   print("Bienvenido Usuario ʕ•́ᴥ•̀ʔっ")
   print("1. Multiplicar lista de numeros por 2")
   print("2. Leer Dias de la Semana")
   print("3. Ingrese numero a la lista")
   print("4. Ingrese dia para eliminar de la lista")
   print("s. Salir")
   opcion=input("Seleccione una opcion: ")
   if opcion =="1":
      multiplicarNumeroPorDos(numeros)
   elif opcion =="2":
      leerDiasDeLaSemana(diasDeLaSemana)
   elif opcion =="3":
      numeroIngresado= int(input("Ingrese numero para agregar a la lista: "))
      numeros.append(numeroIngresado)
   elif opcion =="4":
      diaIngresado = input("Ingrese dia de la semama a eliminar: ")
      diasDeLaSemana.remove(diaIngresado)
      print(diasDeLaSemana)
   elif opcion =="s":
      print("Tenga buen dia")
      break    
   else:
      print("Opcion Incorrecta")

