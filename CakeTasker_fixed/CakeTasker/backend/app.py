
from flask import Flask, request, jsonify
from flask_cors import CORS
from db_manager import DBManager
from pedido import Pedido

app = Flask(__name__)
CORS(app)

db = DBManager()

@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    pedidos = db.obtener_pedidos()
    return jsonify([p.to_json() for p in pedidos])

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.json
    nuevo = Pedido(
        id=None,
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion'),
        estado=data.get('estado', 'pendiente')
    )
    db.insertar_pedido(nuevo)
    return jsonify({"mensaje": "Pedido creado"}), 201

if __name__ == '__main__':
    app.run(debug=True)
