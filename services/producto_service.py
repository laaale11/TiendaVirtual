import json
import os
from models.producto import Producto
from interfaces.producto_interface import IProductoService

class ProductoService(IProductoService):
    def __init__(self, archivo_datos="data/productos.json"):
        self.archivo_datos = archivo_datos
        self._crear_archivo_si_no_existe()
    
    def _crear_archivo_si_no_existe(self):
        os.makedirs(os.path.dirname(self.archivo_datos), exist_ok=True)
        if not os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'w') as f:
                json.dump([], f)
    
    def _cargar_productos(self):
        try:
            with open(self.archivo_datos, 'r') as f:
                datos = json.load(f)
                return [Producto.from_dict(producto) for producto in datos]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _guardar_productos(self, productos):
        with open(self.archivo_datos, 'w') as f:
            json.dump([producto.to_dict() for producto in productos], f, indent=2)
    
    def registrar_producto(self, producto):
        productos = self._cargar_productos()
        # Verificar si el ID ya existe
        if any(p.id_producto == producto.id_producto for p in productos):
            return False, "El ID del producto ya existe"
        
        productos.append(producto)
        self._guardar_productos(productos)
        return True, "Producto registrado exitosamente"
    
    def obtener_producto(self, id_producto):
        productos = self._cargar_productos()
        for producto in productos:
            if producto.id_producto == id_producto:
                return producto
        return None
    
    def obtener_todos_productos(self):
        return self._cargar_productos()
    
    def buscar_productos_por_nombre(self, nombre):
        productos = self._cargar_productos()
        return [p for p in productos if nombre.lower() in p.nombre.lower()]
    
    def actualizar_producto(self, id_producto, datos_actualizados):
        productos = self._cargar_productos()
        for producto in productos:
            if producto.id_producto == id_producto:
                for key, value in datos_actualizados.items():
                    if hasattr(producto, key):
                        setattr(producto, key, value)
                self._guardar_productos(productos)
                return True, "Producto actualizado exitosamente"
        return False, "Producto no encontrado"
    
    def eliminar_producto(self, id_producto):
        productos = self._cargar_productos()
        productos_actualizados = [p for p in productos if p.id_producto != id_producto]
        
        if len(productos_actualizados) == len(productos):
            return False, "Producto no encontrado"
        
        self._guardar_productos(productos_actualizados)
        return True, "Producto eliminado exitosamente"
    
    def obtener_productos_stock_bajo(self):
        productos = self._cargar_productos()
        return [p for p in productos if p.tiene_stock_bajo()]
    
    def actualizar_stock(self, id_producto, cantidad):
        productos = self._cargar_productos()
        for producto in productos:
            if producto.id_producto == id_producto:
                producto.actualizar_stock(cantidad)
                self._guardar_productos(productos)
                return True, "Stock actualizado exitosamente"
        return False, "Producto no encontrado"