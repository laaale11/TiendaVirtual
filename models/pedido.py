from datetime import datetime

class Pedido:
    def __init__(self, id_pedido, id_cliente, productos, total, metodo_pago, comentario="", estado="Pendiente", fecha=None):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.productos = productos
        self.total = total
        self.metodo_pago = metodo_pago
        self.comentario = comentario
        self.estado = estado
        self.fecha = fecha if fecha else datetime.now()
    
    def actualizar_estado(self, nuevo_estado):
        estados_validos = ["Pendiente", "Entregado", "Cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            return True
        return False
    
    def to_dict(self):
        return {
            'id_pedido': self.id_pedido,
            'id_cliente': self.id_cliente,
            'productos': [
                {
                    'id_producto': item['producto'].id_producto,
                    'cantidad': item['cantidad']
                } for item in self.productos
            ],
            'total': self.total,
            'metodo_pago': self.metodo_pago,
            'comentario': self.comentario,
            'estado': self.estado,
            'fecha': self.fecha.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data, productos_dict):
        productos = []
        for item in data['productos']:
            producto = productos_dict.get(item['id_producto'])
            if producto:
                productos.append({'producto': producto, 'cantidad': item['cantidad']})
        
        return cls(
            data['id_pedido'],
            data['id_cliente'],
            productos,
            data['total'],
            data['metodo_pago'],
            data.get('comentario', ''),
            data['estado'],
            datetime.fromisoformat(data['fecha'])
        )
    
    def __str__(self):
        return f"Pedido {self.id_pedido}: ${self.total} - {self.estado} ({self.fecha.strftime('%d/%m/%Y')})"