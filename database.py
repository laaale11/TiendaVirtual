# database.py
import sqlite3
from datetime import datetime
import logging

class DatabaseManager:
    def __init__(self, db_path="tienda_virtual.db"):
        self.db_path = db_path
        self._crear_tablas()
    
    def _crear_tablas(self):
        """Crear las tablas necesarias si no existen"""
        with self._get_connection() as conn:
            # Tabla de productos
            conn.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    precio REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    descripcion TEXT DEFAULT '',
                    categoria TEXT DEFAULT 'general',
                    fecha_creacion TEXT NOT NULL,
                    activo BOOLEAN DEFAULT 1
                )
            ''')
            
            # Tabla de clientes
            conn.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE,
                    telefono TEXT,
                    direccion TEXT,
                    fecha_registro TEXT NOT NULL
                )
            ''')
            
            # Tabla de pedidos
            conn.execute('''
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    fecha_creacion TEXT NOT NULL,
                    estado TEXT NOT NULL DEFAULT 'pendiente',
                    total REAL NOT NULL DEFAULT 0,
                    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
                )
            ''')
            
            # Tabla de items del pedido
            conn.execute('''
                CREATE TABLE IF NOT EXISTS pedido_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pedido_id INTEGER NOT NULL,
                    producto_id INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio_unitario REAL NOT NULL,
                    subtotal REAL NOT NULL,
                    FOREIGN KEY (pedido_id) REFERENCES pedidos (id) ON DELETE CASCADE,
                    FOREIGN KEY (producto_id) REFERENCES productos (id)
                )
            ''')
            
            conn.commit()
    
    def _get_connection(self):
        """Obtener conexión a la base de datos"""
        return sqlite3.connect(self.db_path)