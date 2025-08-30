import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # habilitar CORS

# Función para cargar excel
def cargar_excel(archivo):
    try:
        hojas = pd.read_excel(archivo, sheet_name=None)
        data = {}
        for nombre_hoja, df in hojas.items():
            data[nombre_hoja] = df.fillna("").to_dict(orient="records")
        return data
    except Exception as e:
        return {"error": str(e)}

# Endpoint General: combina todos los Excel
@app.route('/datos_general')
def datos_general():
    archivos = {
        "canada": "TLC COL - CANADA.xlsx",
        "caricom": "TLC COL - CARICOM.xlsx",
        "costarica": "TLC COL - COSTA RICA.xlsx",
        "cuba": "TLC COL - CUBA.xlsx",
        "efta": "TLC COL - EFTA.xlsx",
        "panama": "TLC COL - PANAMA.xlsx",
        "union_europea": "TLC COL - UNIÓN EUROPEA.xlsx"
    }
    data = {}
    for nombre, archivo in archivos.items():
        data[nombre] = cargar_excel(archivo)
    return jsonify(data)

# Endpoint Canadá
@app.route('/datos_canada')
def datos_canada():
    return jsonify(cargar_excel("TLC COL - CANADA.xlsx"))

# Endpoint Caricom
@app.route('/datos_caricom')
def datos_caricom():
    return jsonify(cargar_excel("TLC COL - CARICOM.xlsx"))

# Endpoint Costa Rica
@app.route('/datos_costarica')
def datos_costarica():
    return jsonify(cargar_excel("TLC COL - COSTA RICA.xlsx"))

# Endpoint CUBA
@app.route('/datos_cuba')
def datos_cuba():
    return jsonify(cargar_excel("TLC COL - CUBA.xlsx"))

# Endpoint EFTA
@app.route('/datos_efta')
def datos_efta():
    return jsonify(cargar_excel("TLC COL - EFTA.xlsx"))

# Endpoint PANAMA
@app.route('/datos_panama')
def datos_panama():
    return jsonify(cargar_excel("TLC COL - PANAMA.xlsx"))

# Endpoint Unión Europea
@app.route('/datos_ue')
def datos_ue():
    return jsonify(cargar_excel("TLC COL - UNIÓN EUROPEA.xlsx"))

if __name__ == '__main__':
    app.run(debug=True)
