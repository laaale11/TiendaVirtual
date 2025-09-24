# models.py
from datetime import datetime
from enum import Enum
from typing import List

class EstadoPedido(Enum):
    PENDIENTE = "pendiente"
    CONFIRMADO = "confirmado"
    EN_PREPARACION = "en_preparacion"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"

class Producto:
    def __init__(self, id: int, nombre: str, precio: float, stock: int, 
                 descripcion: str = "", categoria: str = "general"):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.categoria = categoria
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crear Producto desde diccionario (para BD)"""
        return cls(
            id=data['id'],
            nombre=data['nombre'],
            precio=data['precio'],
            stock=data['stock'],
            descripcion=data.get('descripcion', ''),
            categoria=data.get('categoria', 'general')
        )
    
    def to_dict(self):
        """Convertir Producto a diccionario (para BD)"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'descripcion': self.descripcion,
            'categoria': self.categoria
        }

class Cliente:
    def __init__(self, id: int, nombre: str, email: str = "", 
                 telefono: str = "", direccion: str = ""):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            nombre=data['nombre'],
            email=data.get('email', ''),
            telefono=data.get('telefono', ''),
            direccion=data.get('direccion', '')
        )

class ItemPedido:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = producto.precio
    
    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad

class Pedido:
    def __init__(self, id: int, cliente: Cliente, fecha_creacion: datetime = None):
        self.id = id
        self.cliente = cliente
        self.fecha_creacion = fecha_creacion or datetime.now()
        self.items: List[ItemPedido] = []
        self.estado = EstadoPedido.PENDIENTE
        self.total = 0.0
    
    def agregar_item(self, producto: Producto, cantidad: int):
        if producto.stock < cantidad:
            raise ValueError(f"Stock insuficiente para {producto.nombre}")
        
        for item in self.items:
            if item.producto.id == producto.id:
                item.cantidad += cantidad
                self._actualizar_total()
                return
        
        self.items.append(ItemPedido(producto, cantidad))
        self._actualizar_total()
    
    def _actualizar_total(self):
        self.total = sum(item.subtotal for item in self.items)