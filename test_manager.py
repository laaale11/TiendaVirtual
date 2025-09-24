from managers.cliente_manager import ClienteManager, manager_clientes

print("=== PRUEBA COMPLETA DEL CLIENTE MANAGER ===")

# Usar el manager global con datos de ejemplo
manager = manager_clientes

print(f"📊 Clientes cargados: {len(manager.listar_clientes())}")

print(f"\n🎯 PRUEBA DE BÚSQUEDAS:")
print("\n1. Buscar cliente ID 1:")
cliente1 = manager.buscar_por_id(1)
if cliente1:
    print(cliente1.obtener_info())

print("\n2. Buscar por email:")
cliente_email = manager.buscar_por_email("carlos.lopez@email.com")
if cliente_email:
    print(f"Encontrado: {cliente_email.nombre}")

print("\n3. Buscar por nombre 'María':")
resultados = manager.buscar_por_nombre("María")
for c in resultados:
    print(f" - {c.nombre}")

print(f"\n➕ PRUEBA DE AGREGAR CLIENTE:")
try:
    nuevo_cliente = manager.agregar_cliente(
        "Nuevo Cliente", 
        "nuevo@email.com", 
        "Dirección Nueva 999", 
        "555-9999"
    )
    print(f"✅ Cliente agregado: {nuevo_cliente.nombre} (ID: {nuevo_cliente.id})")
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n✏️ PRUEBA DE EDICIÓN:")
try:
    cliente_editado = manager.editar_cliente(1, telefono="555-0000")
    print(f"✅ Cliente editado: Teléfono actualizado a {cliente_editado.telefono}")
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n📈 ESTADÍSTICAS:")
stats = manager.obtener_estadisticas()
for key, value in stats.items():
    print(f"   {key}: {value}")

print(f"\n👥 LISTA DE CLIENTES ACTIVOS:")
clientes_activos = manager.listar_clientes()
print(f"Total activos: {len(clientes_activos)}")
for cliente in clientes_activos[:3]:  # Mostrar primeros 3
    print(f" - {cliente.nombre} ({len(cliente.pedidos)} pedidos)")

print(f"\n🚫 PRUEBA DE DESACTIVAR CLIENTE:")
try:
    resultado = manager.eliminar_cliente(2)
    print(f"✅ {resultado}")
except ValueError as e:
    print(f"❌ Error: {e}")

print(f"\n📊 ESTADÍSTICAS FINALES:")
stats_final = manager.obtener_estadisticas()
print(f"Clientes activos: {stats_final['clientes_activos']}")
print(f"Clientes inactivos: {stats_final['clientes_inactivos']}")

print(f"\n✅ ¡Prueba del ClienteManager completada!")