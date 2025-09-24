# test_database.py
from pedido_manager import PedidoManager
from models import EstadoPedido

def test_base_datos():
    print("=== TEST BASE DE DATOS ===\n")
    
    # Crear manager (creará la BD automáticamente)
    manager = PedidoManager("test_tienda.db")
    
    # Agregar productos de prueba
    print("1. Agregando productos...")
    p1_id = manager.agregar_producto("Laptop Gaming", 1500.0, 10, "Laptop para gaming", "Tecnología")
    p2_id = manager.agregar_producto("Mouse Inalámbrico", 45.0, 50, "Mouse ergonómico", "Tecnología")
    p3_id = manager.agregar_producto("Teclado Mecánico", 120.0, 30, "Teclado RGB", "Tecnología")
    
    print(f"Productos agregados: Laptop (ID: {p1_id}), Mouse (ID: {p2_id}), Teclado (ID: {p3_id})")
    
    # Agregar cliente
    print("\n2. Agregando cliente...")
    cliente_id = manager.agregar_cliente("Ana García", "ana@email.com", "555-1234", "Calle Principal 123")
    print(f"Cliente agregado: Ana García (ID: {cliente_id})")
    
    # Crear pedido
    print("\n3. Creando pedido...")
    pedido = manager.crear_pedido(cliente_id)
    print(f"Pedido creado: #{pedido.id}")
    
    # Agregar productos al pedido
    print("\n4. Agregando productos al pedido...")
    manager.agregar_producto_a_pedido(pedido.id, p1_id, 1)  # 1 Laptop
    manager.agregar_producto_a_pedido(pedido.id, p2_id, 2)  # 2 Mouses
    manager.agregar_producto_a_pedido(pedido.id, p3_id, 1)  # 1 Teclado
    
    # Cambiar estado del pedido
    print("\n5. Cambiando estado del pedido...")
    manager.cambiar_estado_pedido(pedido.id, EstadoPedido.CONFIRMADO)
    print("Estado cambiado a CONFIRMADO")
    
    # Mostrar información
    print("\n6. Mostrando información...")
    
    # Productos
    print("\nProductos en sistema:")
    for producto in manager.productos.values():
        print(f"  - {producto.nombre}: ${producto.precio} (Stock: {producto.stock})")
    
    # Pedidos del cliente
    print(f"\nPedidos del cliente Ana García:")
    pedidos_cliente = manager.obtener_pedidos_por_cliente(cliente_id)
    for pedido in pedidos_cliente:
        print(f"  Pedido #{pedido.id}: ${pedido.total} - {pedido.estado.value}")
        for item in pedido.items:
            print(f"    - {item.cantidad}x {item.producto.nombre}: ${item.subtotal}")
    
    print("\n=== TEST COMPLETADO ===")

if __name__ == "__main__":
    test_base_datos()