from models.cliente import Cliente
from data.clientes_ejemplo import clientes_ejemplo

class ClienteManager:
    def __init__(self, datos_iniciales=None):
        """
        Manager para gestionar clientes
        
        Args:
            datos_iniciales (list): Lista inicial de clientes (opcional)
        """
        self.clientes = datos_iniciales if datos_iniciales else []
        self.ultimo_id = max([c.id for c in self.clientes]) if self.clientes else 0

    def agregar_cliente(self, nombre, email, direccion, telefono=""):
        """Agrega un nuevo cliente"""
        # Validar email único
        if self.buscar_por_email(email):
            raise ValueError(f"Ya existe un cliente con el email: {email}")
        
        self.ultimo_id += 1
        nuevo_cliente = Cliente(self.ultimo_id, nombre, email, direccion, telefono)
        self.clientes.append(nuevo_cliente)
        return nuevo_cliente

    def eliminar_cliente(self, id):
        """Elimina un cliente por ID (desactiva en lugar de eliminar)"""
        cliente = self.buscar_por_id(id)
        if cliente:
            cliente.desactivar()
            return f"Cliente {cliente.nombre} desactivado correctamente"
        else:
            raise ValueError(f"No se encontró cliente con ID: {id}")

    def buscar_por_id(self, id):
        """Busca un cliente por ID"""
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def buscar_por_email(self, email):
        """Busca un cliente por email"""
        for cliente in self.clientes:
            if cliente.email.lower() == email.lower():
                return cliente
        return None

    def buscar_por_nombre(self, nombre):
        """Busca clientes por nombre (búsqueda parcial)"""
        return [cliente for cliente in self.clientes 
                if nombre.lower() in cliente.nombre.lower() and cliente.activo]

    def listar_clientes(self, solo_activos=True):
        """Lista todos los clientes"""
        if solo_activos:
            return [cliente for cliente in self.clientes if cliente.activo]
        return self.clientes

    def editar_cliente(self, id, nombre=None, email=None, direccion=None, telefono=None):
        """Edita la información de un cliente"""
        cliente = self.buscar_por_id(id)
        if not cliente:
            raise ValueError(f"No se encontró cliente con ID: {id}")
        
        # Validar email único si se está cambiando
        if email and email != cliente.email:
            if self.buscar_por_email(email):
                raise ValueError(f"Ya existe un cliente con el email: {email}")
        
        cliente.editar_informacion(nombre, email, direccion, telefono)
        return cliente

    def obtener_estadisticas(self):
        """Obtiene estadísticas de los clientes"""
        total_clientes = len(self.clientes)
        clientes_activos = len([c for c in self.clientes if c.activo])
        clientes_con_pedidos = len([c for c in self.clientes if c.pedidos])
        total_pedidos = sum(len(c.pedidos) for c in self.clientes)
        
        return {
            "total_clientes": total_clientes,
            "clientes_activos": clientes_activos,
            "clientes_inactivos": total_clientes - clientes_activos,
            "clientes_con_pedidos": clientes_con_pedidos,
            "total_pedidos": total_pedidos,
            "promedio_pedidos_por_cliente": total_pedidos / clientes_con_pedidos if clientes_con_pedidos else 0
        }

    def activar_cliente(self, id):
        """Reactiva un cliente desactivado"""
        cliente = self.buscar_por_id(id)
        if cliente:
            cliente.activar()
            return f"Cliente {cliente.nombre} reactivado correctamente"
        else:
            raise ValueError(f"No se encontró cliente con ID: {id}")

    def exportar_clientes(self, solo_activos=True):
        """Exporta la lista de clientes a un formato legible"""
        clientes = self.listar_clientes(solo_activos)
        
        resultado = "=== LISTA DE CLIENTES ===\n"
        for cliente in clientes:
            resultado += f"\n{cliente.obtener_info()}\n"
            resultado += "-" * 50
        
        return resultado

# Crear instancia global con datos de ejemplo
manager_clientes = ClienteManager(clientes_ejemplo)

if __name__ == "__main__":
    print("=== PRUEBA DEL CLIENTE MANAGER ===")
    print(f"Clientes cargados: {len(manager_clientes.clientes)}")
    
    # Probar funcionalidades
    print("\n1. Buscar cliente por ID 1:")
    cliente = manager_clientes.buscar_por_id(1)
    if cliente:
        print(cliente.obtener_info())
    
    print("\n2. Buscar por nombre 'Ana':")
    resultados = manager_clientes.buscar_por_nombre("Ana")
    for c in resultados:
        print(f" - {c.nombre} ({c.email})")
    
    print("\n3. Estadísticas:")
    stats = manager_clientes.obtener_estadisticas()
    for key, value in stats.items():
        print(f"   {key}: {value}")