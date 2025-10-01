import json
import os
from datetime import datetime
from models.pedido import Pedido
from interfaces.pedido_interface import IPedidoService

class PedidoService(IPedidoService):
    def __init__(self, archivo_datos="data/pedidos.json", producto_service=None):
        self.archivo_datos = archivo_datos
        self.producto_service = producto_service
        self._crear_archivo_si_no_existe()
    
    def _crear_archivo_si_no_existe(self):
        os.makedirs(os.path.dirname(self.archivo_datos), exist_ok=True)
        if not os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'w') as f:
                json.dump([], f)
    
    def _cargar_pedidos(self):
        try:
            with open(self.archivo_datos, 'r') as f:
                datos = json.load(f)
                
            if self.producto_service:
                productos_dict = {p.id_producto: p for p in self.producto_service.obtener_todos_productos()}
                return [Pedido.from_dict(pedido, productos_dict) for pedido in datos]
            else:
                return []
                
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _guardar_pedidos(self, pedidos):
        with open(self.archivo_datos, 'w') as f:
            json.dump([pedido.to_dict() for pedido in pedidos], f, indent=2)
    
    def registrar_pedido(self, pedido):
        pedidos = self._cargar_pedidos()
        
        if any(p.id_pedido == pedido.id_pedido for p in pedidos):
            return False, "El ID del pedido ya existe"
        
        # Verificar stock y actualizar
        for item in pedido.productos:
            producto = item['producto']
            cantidad = item['cantidad']
            if producto.stock < cantidad:
                return False, f"Stock insuficiente para {producto.nombre}"
            
            self.producto_service.actualizar_stock(producto.id_producto, -cantidad)
        
        pedidos.append(pedido)
        self._guardar_pedidos(pedidos)
        return True, "Pedido registrado exitosamente"
    
    def obtener_pedido(self, id_pedido):
        pedidos = self._cargar_pedidos()
        for pedido in pedidos:
            if pedido.id_pedido == id_pedido:
                return pedido
        return None
    
    def obtener_todos_pedidos(self):
        return self._cargar_pedidos()
    
    def actualizar_estado_pedido(self, id_pedido, nuevo_estado):
        pedidos = self._cargar_pedidos()
        for pedido in pedidos:
            if pedido.id_pedido == id_pedido:
                if pedido.actualizar_estado(nuevo_estado):
                    self._guardar_pedidos(pedidos)
                    return True, f"Estado actualizado a {nuevo_estado}"
                else:
                    return False, "Estado inválido"
        return False, "Pedido no encontrado"
    
    def cancelar_pedido(self, id_pedido):
        pedidos = self._cargar_pedidos()
        for pedido in pedidos:
            if pedido.id_pedido == id_pedido:
                if pedido.estado != "Cancelado":
                    for item in pedido.productos:
                        producto = item['producto']
                        cantidad = item['cantidad']
                        self.producto_service.actualizar_stock(producto.id_producto, cantidad)
                
                pedido.estado = "Cancelado"
                self._guardar_pedidos(pedidos)
                return True, "Pedido cancelado exitosamente"
        return False, "Pedido no encontrado"
    
    def obtener_pedidos_por_cliente(self, id_cliente):
        pedidos = self._cargar_pedidos()
        return [p for p in pedidos if p.id_cliente == id_cliente]
    
    def obtener_pedidos_por_fecha(self, fecha):
        pedidos = self._cargar_pedidos()
        return [p for p in pedidos if p.fecha.date() == fecha.date()]
    
    def calcular_total_pedido(self, productos):
        total = 0
        for item in productos:
            producto = item['producto']
            cantidad = item['cantidad']
            total += producto.precio_unidad * cantidad
        return total