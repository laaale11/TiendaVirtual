from datetime import datetime

class Comunicacion:
    def __init__(self, id_comunicacion, id_cliente, tipo, mensaje, medio, fecha=None):
        self.id_comunicacion = id_comunicacion
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.mensaje = mensaje
        self.medio = medio
        self.fecha = fecha if fecha else datetime.now()
    
    def to_dict(self):
        return {
            'id_comunicacion': self.id_comunicacion,
            'id_cliente': self.id_cliente,
            'tipo': self.tipo,
            'mensaje': self.mensaje,
            'medio': self.medio,
            'fecha': self.fecha.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id_comunicacion'],
            data['id_cliente'],
            data['tipo'],
            data['mensaje'],
            data['medio'],
            datetime.fromisoformat(data['fecha'])
        )
    
    def __str__(self):
        return f"{self.tipo} a {self.medio}: {self.mensaje[:30]}..."
    