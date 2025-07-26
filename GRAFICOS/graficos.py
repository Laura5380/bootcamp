import matplotlib.pyplot as plt
import pymysql.cursors
import pandas as pd
db = pymysql.connect(
    host="localhost",
    user="root",           
    password="Laura225380.",     
    database="sabadoJulio" 
)
cursor = db.cursor(dictionary=True)
resultadosPersonas= []
cursor.execute("SELECT * FROM persona")
resultadosPersonas = cursor.fetchall()
print(resultadosPersonas)
personas = pd.DataFrame(resultadosPersonas)
print (personas)


nombre = ["Jorge","Ana","Laura"]
edad = [31,26,24]

plt.plot(personas['nombre'],personas['edad'])
plt.title("Grafico de edad por persona")
plt.show()

plt.bar(nombre,edad)
plt.title("Grafico de edad por persona")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

plt.scatter(nombre,edad)
plt.title("Grafico de dispersión - edad por persona")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

divisa = ["USD","EUR","GBP","CAD"]
valor = [4.108,4.776,5.480,2.967]

plt.plot(divisa,valor)
plt.title("Grafico Divisas a Pesos colombianos")
plt.show()

plt.bar(divisa,valor)
plt.title("Grafico Divisas a Pesos colombianos")
plt.xlabel("Divisa")
plt.ylabel("Valor")
plt.show()

plt.scatter(divisa,valor)
plt.title("Grafico de dispersión - Divisas a Pesos colombianos")
plt.xlabel("Divisa")
plt.ylabel("Valor")
plt.show()

#ventas por mes
labels = ["Marzo","Abril","Mayo","Junio"]
sizes = [23,56,12,32]

plt.pie(sizes,labels = labels, autopct= '%1.1f%%',startangle=90)
plt.title("Gráfico de torta de ventas por mes")
plt.show()

#finanzas personales
labels = ["Alimentación","Vivienda","Transporte","Ocio"]
sizes = [300.000,650.000,140.000,200.000]

plt.pie(sizes,labels = labels, autopct= '%1.1f%%',startangle=90)
plt.title("Gráfico de torta - Finanzas Personales")
plt.show()

