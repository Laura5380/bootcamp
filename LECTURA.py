import pandas as pd
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que tu JS consuma la API desde el navegador

@app.route('/')
def index():
    # Renderiza tu archivo index.html (asegúrate que esté en la carpeta /templates)
    return render_template('index.html')

@app.route('/datos')
def obtener_datos():
    # Nombre del archivo Excel
    archivo = "TLC COL - UNIÓN EUROPEA.xlsx"

    # Cargar todas las hojas en un diccionario {nombre_hoja: DataFrame}
    hojas = pd.read_excel(archivo, sheet_name=None)

    # Convertir cada hoja a lista de diccionarios
    data = {}
    for nombre_hoja, df in hojas.items():
        data[nombre_hoja] = df.fillna("").to_dict(orient="records")

    # Retornar el JSON con todas las pestañas
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

