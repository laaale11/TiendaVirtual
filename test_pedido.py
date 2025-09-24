from models.pedido import Pedido

print("=== PRUEBA DE LA CLASE PEDIDO ===")

# Crear un pedido de prueba
pedido1 = Pedido(1, 101)  # Pedido ID 1, Cliente ID 101

print("\n1. Pedido creado:")
print(pedido1)

print("\n2. Agregar productos:")
print(pedido1.agregar_producto("Laptop HP", 1200.50))
print(pedido1.agregar_producto("Mouse inalámbrico", 25.99))
print(pedido1.agregar_producto("Case para laptop", 35.75))

print("\n3. Información detallada del pedido:")
print(pedido1.obtener_info_detallada())

print("\n4. Probar cambio de estado:")
print(pedido1.cambiar_estado("confirmado"))

print("\n5. Probar descuento:")
print(pedido1.aplicar_descuento(10))

print("\n6. Verificar si está activo:")
print(f"¿Pedido activo? {pedido1.esta_activo()}")

print("\n7. Probar eliminar producto:")
print(pedido1.eliminar_producto(1))  # Eliminar el segundo producto (Mouse)

print("\nInformación final:")
print(pedido1.obtener_info_detallada())

print("\n✅ ¡Prueba de Pedido completada exitosamente!")
