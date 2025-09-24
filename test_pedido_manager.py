from managers.pedido_manager import PedidoManager, manager_pedidos
from managers.cliente_manager import manager_clientes

print("=== PRUEBA COMPLETA DEL PEDIDO MANAGER ===")

# Usar el manager global con datos de ejemplo
manager = manager_pedidos

print(f"📦 Pedidos cargados: {len(manager.pedidos)}")

print(f"\n🎯 PRUEBA DE BÚSQUEDAS:")
print("\n1. Buscar pedido ID 1:")
pedido1 = manager.buscar_por_id(1)
if pedido1:
    print(pedido1.obtener_info_detallada())

print("\n2. Buscar pedidos del cliente ID 1:")
pedidos_cliente = manager.buscar_por_cliente(1)
print(f"Pedidos encontrados: {len(pedidos_cliente)}")
for p in pedidos_cliente:
    print(f" - Pedido #{p.id}: ${p.total:.2f} ({p.estado})")

print(f"\n➕ PRUEBA DE CREAR NUEVO PEDIDO:")
try:
    nuevo_pedido = manager.crear_pedido(1)  # Cliente ID 1 (Ana García)
    print(f"✅ Pedido creado: #{nuevo_pedido.id} para cliente {nuevo_pedido.cliente_id}")
    
    # Agregar productos al nuevo pedido
    manager.agregar_producto_pedido(nuevo_pedido.id, "Laptop Gaming", 1200.00)
    manager.agregar_producto_pedido(nuevo_pedido.id, "Monitor 27\"", 300.00)
    print(f"✅ Productos agregados. Total: ${nuevo_pedido.total:.2f}")
    
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n✏️ PRUEBA DE CAMBIAR ESTADO:")
try:
    resultado = manager.cambiar_estado_pedido(1, "enviado")
    print(f"✅ {resultado}")
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n💰 PRUEBA DE DESCUENTO:")
try:
    resultado = manager.aplicar_descuento_pedido(2, 10)  # 10% de descuento
    print(f"✅ {resultado}")
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n📈 ESTADÍSTICAS COMPLETAS:")
stats = manager.obtener_estadisticas()
for key, value in stats.items():
    if key != "pedidos_por_estado":
        print(f"   {key}: {value}")

print("   pedidos_por_estado:")
for estado, cantidad in stats["pedidos_por_estado"].items():
    print(f"     {estado}: {cantidad}")

print(f"\n🔍 PEDIDOS POR ESTADO:")
estados = ["pendiente", "confirmado", "enviado", "entregado", "cancelado"]
for estado in estados:
    pedidos_estado = manager.listar_pedidos(estado=estado)
    print(f"   {estado}: {len(pedidos_estado)} pedidos")

print(f"\n🚫 PRUEBA DE CANCELAR PEDIDO:")
try:
    resultado = manager.cancelar_pedido(3)
    print(f"✅ {resultado}")
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n📊 PEDIDOS ACTIVOS:")
activos = manager.obtener_pedidos_activos()
print(f"Total de pedidos activos: {len(activos)}")
for pedido in activos[:3]:  # Mostrar primeros 3
    print(f" - Pedido #{pedido.id}: ${pedido.total:.2f} ({pedido.estado})")

print(f"\n✅ ¡Prueba del PedidoManager completada!")