from flask import Flask, jsonify,request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

ListaPersonas=[]
resultadosPersonas =[]

db = pymysql.connect(
    host="localhost",
    user="root",          
    password="Laura225380.",    
    database="sabadoJulio"
)
cursor = db.cursor(pymysql.cursors.DictCursor)

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicación Web'

@app.route('/ListaPersonas',methods=['GET'])
def listar():
    return jsonify(ListaPersonas)
#Listar
@app.route('/datosBase',methods=['GET'])
def datosBase():
    cursor.execute("SELECT * FROM persona")
    resultadosPersonas = cursor.fetchall()
    return jsonify(resultadosPersonas)
#Agregar
@app.route('/AgregarPersona',methods=['POST'])
def agregar():
    NuevaPersona= request.json.get('persona')
    ListaPersonas.append(NuevaPersona)
    cursor.execute('INSERT INTO persona(identificacion,edad,nombre) values (%s, %s, %s)',
                   (NuevaPersona['identificacion'], NuevaPersona['edad'],NuevaPersona['nombre']))
    db.commit()
    return "Se agrego una nueva persona"
#Buscar 
@app.route('/BuscarPersonas/<identificacion>', methods=['GET'])
def buscar(identificacion):
    cursor.execute("SELECT * FROM persona WHERE identificacion = %s",(identificacion,))
    resultadosPersonas =cursor.fetchall()
    return jsonify(resultadosPersonas)
#Actualizar
@app.route('/ActualizarPersonas/<identificacion>', methods=['PUT'])
def actualizar(identificacion):
    datos_nuevos = request.json
    cursor.execute("UPDATE persona SET nombre=%s,edad=%s WHERE identificacion=%s",
    (datos_nuevos['nombre'],datos_nuevos['edad'],datos_nuevos['identificacion']))
    db.commit()
    return "Persona Actualizada"
#Eliminar
@app.route('/EliminarPersonas/<identificacion>', methods=['DELETE'])
def eliminar(identificacion):
    cursor.execute('DELETE FROM persona WHERE identificacion=%s',
    (identificacion,))
    db.commit()
    return "Persona Eliminada"

if __name__ == '__main__':
   app.run(debug=True)