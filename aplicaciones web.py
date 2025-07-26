import pandas as pd
datos = pd.read_excel("Estudiantes.xlsx")

from flask import Flask, jsonify

app = Flask (__name__)

app.route('mensaje',methods=['GET'])
def mensaje():
    return 'primera aplicacion web'

app.route('/datos',methods=['GET'])
def datos():
    return jsonify(datos)


"""
@app.route('/codigos',methods=['GET'])
def CodigosArancelarios(): 
"""    

if __name__ == '__main__':
   app.run(debug=True)