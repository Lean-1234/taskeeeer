
import sqlite3
from pedido import Pedido

class DBManager:
    def __init__(self, db_name='cake.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.crear_tabla()

    def crear_tabla(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                descripcion TEXT,
                estado TEXT
            )
        ''')
        self.conn.commit()

    def insertar_pedido(self, pedido):
        self.conn.execute(
            "INSERT INTO pedidos (nombre, descripcion, estado) VALUES (?, ?, ?)",
            (pedido.nombre, pedido.descripcion, pedido.estado)
        )
        self.conn.commit()

    def obtener_pedidos(self):
        cursor = self.conn.execute("SELECT id, nombre, descripcion, estado FROM pedidos")
        pedidos = []
        for row in cursor.fetchall():
            pedidos.append(Pedido(id=row[0], nombre=row[1], descripcion=row[2], estado=row[3]))
        return pedidos
