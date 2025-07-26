import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",           
    password="Laura225380.",     
    database="sabadoJulio" 
)
cursor = db.cursor()

query = "SELECT * FROM persona"

try:
    cursor.execute(query)
    resultados = cursor.fetchall()   
    print("Datos de la tabla estudiantes:")
    for persona in resultados:
        print(persona)

except pymysql.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    db.close()
