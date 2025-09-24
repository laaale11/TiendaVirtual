from models.cliente import Cliente

print("=== PRUEBA DE LA CLASE CLIENTE ===")

# Crear clientes de prueba
cliente1 = Cliente(1, "Ana García", "ana@email.com", "Calle 123, Ciudad", "555-1234")
cliente2 = Cliente(2, "Carlos López", "carlos@email.com", "Avenida 456, Ciudad")

print("\n1. Mostrar clientes:")
print(cliente1)
print(cliente2)

print("\n2. Información detallada:")
print(cliente1.obtener_info())

print("\n3. Probar edición de información:")
cliente1.editar_informacion(telefono="555-5678")
print("Teléfono actualizado:")
print(cliente1.obtener_info())

print("\n4. Probar agregar pedido:")
cliente1.agregar_pedido(101)
cliente1.agregar_pedido(102)
print(f"Pedidos de {cliente1.nombre}: {cliente1.pedidos}")

print("\n✅ ¡Prueba completada exitosamente!")