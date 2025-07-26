
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mensaje',methods=['GET'])
def mensaje():
    return 'BIENVENIDO A COL TLC :)'

if __name__ == '__main__':
   app.run(debug=True)