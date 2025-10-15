class Cliente:
    def __init__(self, id_cliente, nombre, celular, direccion, ciudad, email, tipo_cliente="Minorista", activo=True):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.celular = celular
        self.direccion = direccion
        self.ciudad = ciudad
        self.email = email
        self.tipo_cliente = tipo_cliente
        self.activo = activo  # Nuevo: estado activo/inactivo
    
    def to_dict(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'celular': self.celular,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'email': self.email,
            'tipo_cliente': self.tipo_cliente,
            'activo': self.activo  # Nuevo campo
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id_cliente'],
            data['nombre'],
            data['celular'],
            data['direccion'],
            data['ciudad'],
            data['email'],
            data.get('tipo_cliente', 'Minorista'),
            data.get('activo', True)  # Nuevo campo
        )
    
    def __str__(self):
        estado = "✅" if self.activo else "❌"
        tipo_icon = "🏢" if self.tipo_cliente == "Mayorista" else "👤"
        return f"{estado} {tipo_icon} {self.id_cliente}: {self.nombre} ({self.tipo_cliente})"