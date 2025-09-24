class Cliente:
    def __init__(self, id, nombre, email, direccion, telefono=""):
        """
        Constructor de la clase Cliente
        
        Args:
            id (int): Identificador único del cliente
            nombre (str): Nombre completo del cliente
            email (str): Correo electrónico
            direccion (str): Dirección de entrega
            telefono (str, optional): Número de teléfono. Defaults to "".
        """
        self.id = id
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.pedidos = []  # Lista para almacenar los pedidos del cliente
        self.activo = True  # Estado del cliente (activo/inactivo)

    def __str__(self):
        """Representación en string del cliente"""
        return f"Cliente {self.id}: {self.nombre} | {self.email}"

    def obtener_info(self):
        """Obtiene información detallada del cliente"""
        estado = "Activo" if self.activo else "Inactivo"
        info = f"""
        === INFORMACIÓN DEL CLIENTE ===
        ID: {self.id}
        Nombre: {self.nombre}
        Email: {self.email}
        Dirección: {self.direccion}
        Teléfono: {self.telefono if self.telefono else 'No registrado'}
        Estado: {estado}
        Pedidos realizados: {len(self.pedidos)}
        """
        return info

    def agregar_pedido(self, pedido_id):
        """Agrega un pedido a la lista del cliente"""
        self.pedidos.append(pedido_id)

    def desactivar(self):
        """Desactiva el cliente"""
        self.activo = False

    def activar(self):
        """Activa el cliente"""
        self.activo = True

    def editar_informacion(self, nombre=None, email=None, direccion=None, telefono=None):
        """Edita la información del cliente"""
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
            