from data.clientes_ejemplo import clientes_ejemplo, pedidos_ejemplo

print("=== PRUEBA DE DATOS DE EJEMPLO ===")

print(f"\n📊 ESTADÍSTICAS:")
print(f"Total de clientes: {len(clientes_ejemplo)}")
print(f"Total de pedidos: {len(pedidos_ejemplo)}")

print(f"\n👥 CLIENTES ACTIVOS:")
clientes_activos = [c for c in clientes_ejemplo if c.activo]
clientes_inactivos = [c for c in clientes_ejemplo if not c.activo]

print(f"Clientes activos: {len(clientes_activos)}")
print(f"Clientes inactivos: {len(clientes_inactivos)}")

print(f"\n📦 PEDIDOS POR ESTADO:")
from collections import Counter
estados_pedidos = Counter(pedido.estado for pedido in pedidos_ejemplo)
for estado, cantidad in estados_pedidos.items():
    print(f"  {estado}: {cantidad} pedidos")

print(f"\n💰 TOTAL EN VENTAS:")
venta_total = sum(pedido.total for pedido in pedidos_ejemplo)
print(f"Venta total: ${venta_total:.2f}")

print(f"\n🎯 CLIENTE CON MÁS PEDIDOS:")
cliente_mas_pedidos = max(clientes_ejemplo, key=lambda c: len(c.pedidos))
print(f"{cliente_mas_pedidos.nombre}: {len(cliente_mas_pedidos.pedidos)} pedidos")

print(f"\n🔍 MUESTRA DE DATOS:")
print("\n--- Primeros 3 clientes ---")
for i, cliente in enumerate(clientes_ejemplo[:3], 1):
    print(f"{i}. {cliente}")

print("\n--- Primeros 2 pedidos ---")
for i, pedido in enumerate(pedidos_ejemplo[:2], 1):
    print(f"{i}. {pedido}")

print("\n✅ ¡Datos de ejemplo cargados correctamente!")