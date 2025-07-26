from flask import Flask, jsonify,request
from flask_cors import CORS
import pymysql.cursors
app = Flask(__name__)
CORS(app)

ListaPersonas = []

import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",           
    password="Laura225380.",     
    database="sabadoJulio" 
)
cursor = db.cursor(pymysql.cursors.DictCursor)

query = "SELECT * FROM persona"


@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'Primera aplicación Web'


@app.route('/listarpersonas',methods=['GET'])
def listar():
    return jsonify(ListaPersonas)


@app.route('/agregarPersona',methods=['POST'])
def agregar():
    nuevaPersona = request.json.get('persona')
    ListaPersonas.append(nuevaPersona)
    return 'Se agrego una nueva persona'

@app.route('/datosDeLaRuta',methods=['GET'])
def datosBase():
    cursor.execute(query)
    resultadosPersonas = cursor.fetchall()
    return jsonify(resultadosPersonas)

@app.route('/AgregarPersonaBD',methods=['POST'])
def agregarbd():
    NuevaPersona= request.json.get('persona')
    ListaPersonas.append(NuevaPersona)
    cursor.execute('INSERT INTO persona(identificacion,nombre,edad) values (%s, %s, %s)',
                   (NuevaPersona['identificacion'],NuevaPersona['nombre'], NuevaPersona['edad']))
    db.commit()
    return "Se agrego una nueva persona"

if __name__ == '__main__':
   app.run(debug=True)