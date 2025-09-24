from models.cliente import Cliente
from models.pedido import Pedido

def crear_datos_ejemplo():
    """Crea datos de ejemplo para pruebas"""
    
    # Crear clientes de ejemplo
    clientes = [
        Cliente(1, "Ana García", "ana.garcia@email.com", "Calle Primavera 123, Ciudad", "555-0101"),
        Cliente(2, "Carlos López", "carlos.lopez@email.com", "Avenida Central 456, Ciudad", "555-0102"),
        Cliente(3, "María Rodríguez", "maria.rodriguez@email.com", "Plaza Mayor 789, Ciudad", "555-0103"),
        Cliente(4, "Juan Martínez", "juan.martinez@email.com", "Boulevard Norte 321, Ciudad", ""),
        Cliente(5, "Laura Fernández", "laura.fernandez@email.com", "Camino Real 654, Ciudad", "555-0105"),
        Cliente(6, "Diego Silva", "diego.silva@email.com", "Río Azul 987, Ciudad", "555-0106"),
        Cliente(7, "Sofía Castro", "sofia.castro@email.com", "Montaña Verde 147, Ciudad", "555-0107"),
        Cliente(8, "Pedro Navarro", "pedro.navarro@email.com", "Lago Sereno 258, Ciudad", "555-0108")
    ]
    
    # Crear pedidos de ejemplo
    pedidos = [
        Pedido(1, 1),  # Pedido para Ana García
        Pedido(2, 2),  # Pedido para Carlos López
        Pedido(3, 1),  # Otro pedido para Ana García
        Pedido(4, 3),  # Pedido para María Rodríguez
        Pedido(5, 5)   # Pedido para Laura Fernández
    ]
    
    # Agregar productos a los pedidos
    pedidos[0].agregar_producto("Laptop HP Pavilion", 850.00)
    pedidos[0].agregar_producto("Mouse inalámbrico", 25.99)
    pedidos[0].cambiar_estado("entregado")
    
    pedidos[1].agregar_producto("Smartphone Samsung Galaxy", 450.50)
    pedidos[1].agregar_producto("Funda protectora", 15.75)
    pedidos[1].agregar_producto("Protector pantalla", 8.99)
    pedidos[1].cambiar_estado("enviado")
    
    pedidos[2].agregar_producto("Tablet iPad", 320.00)
    pedidos[2].agregar_producto("Teclado Bluetooth", 45.00)
    
    pedidos[3].agregar_producto("Monitor 24 pulgadas", 180.00)
    pedidos[3].cambiar_estado("confirmado")
    
    pedidos[4].agregar_producto("Auriculares inalámbricos", 89.99)
    pedidos[4].agregar_producto("Cargador rápido", 22.50)
    
    # Asignar pedidos a clientes
    clientes[0].agregar_pedido(1)  # Ana tiene pedidos 1 y 3
    clientes[0].agregar_pedido(3)
    clientes[1].agregar_pedido(2)  # Carlos tiene pedido 2
    clientes[2].agregar_pedido(4)  # María tiene pedido 4
    clientes[4].agregar_pedido(5)  # Laura tiene pedido 5
    
    # Desactivar un cliente de ejemplo
    clientes[7].desactivar()  # Pedro Navarro está inactivo
    
    return clientes, pedidos

# Datos disponibles para importar
clientes_ejemplo, pedidos_ejemplo = crear_datos_ejemplo()

if __name__ == "__main__":
    print("=== DATOS DE EJEMPLO CARGADOS ===")
    print(f"Clientes creados: {len(clientes_ejemplo)}")
    print(f"Pedidos creados: {len(pedidos_ejemplo)}")
    
    print("\n--- Clientes activos ---")
    for cliente in clientes_ejemplo:
        if cliente.activo:
            print(f"{cliente.nombre} - {len(cliente.pedidos)} pedidos")
    
    print("\n--- Pedidos por estado ---")
    estados = {}
    for pedido in pedidos_ejemplo:
        estados[pedido.estado] = estados.get(pedido.estado, 0) + 1
    
    for estado, cantidad in estados.items():
        print(f"{estado}: {cantidad} pedidos")