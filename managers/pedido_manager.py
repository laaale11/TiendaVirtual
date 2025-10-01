from services.pedido_service import PedidoService
from services.producto_service import ProductoService
from services.cliente_service import ClienteService
from models.pedido import Pedido
from datetime import datetime

class PedidoManager:
    def __init__(self):
        self.producto_service = ProductoService()
        self.cliente_service = ClienteService()
        self.pedido_service = PedidoService(producto_service=self.producto_service)
    
    def registrar_pedido(self):
        print("\n=== REGISTRAR NUEVO PEDIDO ===")
        
        # Verificar que hay productos y clientes
        productos = self.producto_service.obtener_todos_productos()
        clientes = self.cliente_service.obtener_todos_clientes()
        
        if not productos:
            print("❌ No hay productos registrados. Registra productos primero.")
            return
        
        if not clientes:
            print("❌ No hay clientes registrados. Registra clientes primero.")
            return
        
        id_pedido = input("ID del pedido: ")
        id_cliente = input("ID del cliente: ")
        
        # Verificar cliente
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        # Seleccionar productos
        productos_pedido = []
        print("\n🛒 SELECCIONAR PRODUCTOS:")
        self._mostrar_productos_disponibles()
        
        while True:
            id_producto = input("\nID del producto (o 'fin' para terminar): ")
            if id_producto.lower() == 'fin':
                break
            
            producto = self.producto_service.obtener_producto(id_producto)
            if not producto:
                print("❌ Producto no encontrado.")
                continue
            
            cantidad = int(input(f"Cantidad de {producto.nombre}: "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0.")
                continue
            
            productos_pedido.append({'producto': producto, 'cantidad': cantidad})
            print(f"✅ Agregado: {producto.nombre} x {cantidad}")
        
        if not productos_pedido:
            print("❌ El pedido debe tener al menos un producto.")
            return
        
        # Método de pago
        print("\n💳 MÉTODO DE PAGO:")
        print("  1. Efectivo")
        print("  2. Transferencia")
        print("  3. Otro")
        metodo_opcion = input("Selecciona método (1-3): ")
        metodos = {"1": "Efectivo", "2": "Transferencia", "3": "Otro"}
        metodo_pago = metodos.get(metodo_opcion, "Efectivo")
        
        comentario = input("Comentario (opcional): ")
        
        # Calcular total
        total = self.pedido_service.calcular_total_pedido(productos_pedido)
        
        # Crear pedido
        pedido = Pedido(id_pedido, id_cliente, productos_pedido, total, metodo_pago, comentario)
        success, message = self.pedido_service.registrar_pedido(pedido)
        
        print(f"\n{'✅' if success else '❌'} {message}")
        if success:
            print(f"📦 Total del pedido: ${total}")
            print(f"💳 Método de pago: {metodo_pago}")
    
    def _mostrar_productos_disponibles(self):
        productos = self.producto_service.obtener_todos_productos()
        print("Productos disponibles:")
        for producto in productos:
            stock_icon = "⚠️" if producto.tiene_stock_bajo() else "✅"
            print(f"   {stock_icon} {producto.id_producto}: {producto.nombre} - Uni:${producto.precio_unidad} (Stock: {producto.stock})")
    
    def ver_pedidos(self):
        print("\n=== PEDIDOS REGISTRADOS ===")
        pedidos = self.pedido_service.obtener_todos_pedidos()
        
        if not pedidos:
            print("No hay pedidos registrados.")
            return
        
        print(f"\n{'ID PEDIDO':<12} {'CLIENTE':<20} {'FECHA':<12} {'TOTAL':<10} {'ESTADO':<12} {'PAGO':<12}")
        print("=" * 85)
        
        for pedido in pedidos:
            cliente = self.cliente_service.obtener_cliente(pedido.id_cliente)
            nombre_cliente = cliente.nombre if cliente else "No encontrado"
            estado_icon = "🟡" if pedido.estado == "Pendiente" else "🟢" if pedido.estado == "Entregado" else "🔴"
            
            print(f"{pedido.id_pedido:<12} {nombre_cliente:<20} {pedido.fecha.strftime('%d/%m/%Y'):<12} ${pedido.total:<9} {estado_icon} {pedido.estado:<10} {pedido.metodo_pago:<12}")
    
    def buscar_pedido(self):
        print("\n=== BUSCAR PEDIDO ===")
        id_pedido = input("ID del pedido: ")
        
        pedido = self.pedido_service.obtener_pedido(id_pedido)
        if not pedido:
            print("❌ Pedido no encontrado.")
            return
        
        cliente = self.cliente_service.obtener_cliente(pedido.id_cliente)
        print(f"\n✅ PEDIDO ENCONTRADO:")
        print(f"   ID: {pedido.id_pedido}")
        print(f"   Cliente: {cliente.nombre if cliente else 'No encontrado'}")
        print(f"   Fecha: {pedido.fecha.strftime('%d/%m/%Y %H:%M')}")
        print(f"   Estado: {pedido.estado}")
        print(f"   Total: ${pedido.total}")
        print(f"   Método de pago: {pedido.metodo_pago}")
        print(f"   Comentario: {pedido.comentario}")
        print(f"   Productos:")
        for item in pedido.productos:
            print(f"     - {item['producto'].nombre} x {item['cantidad']} = ${item['producto'].precio_unidad * item['cantidad']}")
    
    def actualizar_estado(self):
        print("\n=== ACTUALIZAR ESTADO DEL PEDIDO ===")
        id_pedido = input("ID del pedido: ")
        
        pedido = self.pedido_service.obtener_pedido(id_pedido)
        if not pedido:
            print("❌ Pedido no encontrado.")
            return
        
        print(f"\nEstado actual: {pedido.estado}")
        print("Estados disponibles:")
        print("  1. Pendiente")
        print("  2. Entregado")
        print("  3. Cancelado")
        
        estado_opcion = input("Nuevo estado (1-3): ")
        estados = {"1": "Pendiente", "2": "Entregado", "3": "Cancelado"}
        nuevo_estado = estados.get(estado_opcion, pedido.estado)
        
        success, message = self.pedido_service.actualizar_estado_pedido(id_pedido, nuevo_estado)
        print(f"\n{'✅' if success else '❌'} {message}")
    
    def cancelar_pedido(self):
        print("\n=== CANCELAR PEDIDO ===")
        id_pedido = input("ID del pedido a cancelar: ")
        
        pedido = self.pedido_service.obtener_pedido(id_pedido)
        if not pedido:
            print("❌ Pedido no encontrado.")
            return
        
        if pedido.estado == "Cancelado":
            print("❌ El pedido ya está cancelado.")
            return
        
        confirmacion = input(f"¿Estás seguro de cancelar el pedido {id_pedido}? (s/n): ")
        if confirmacion.lower() == 's':
            success, message = self.pedido_service.cancelar_pedido(id_pedido)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ Cancelación cancelada.")
    
    def ver_pedidos_cliente(self):
        print("\n=== PEDIDOS POR CLIENTE ===")
        id_cliente = input("ID del cliente: ")
        
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        pedidos = self.pedido_service.obtener_pedidos_por_cliente(id_cliente)
        
        if not pedidos:
            print(f"📭 El cliente {cliente.nombre} no tiene pedidos.")
            return
        
        print(f"\n📦 PEDIDOS DE {cliente.nombre.upper()}:")
        for pedido in pedidos:
            estado_icon = "🟡" if pedido.estado == "Pendiente" else "🟢" if pedido.estado == "Entregado" else "🔴"
            print(f"   {estado_icon} {pedido.id_pedido}: ${pedido.total} - {pedido.estado} ({pedido.fecha.strftime('%d/%m/%Y')})")
    
    def ver_pedidos_fecha(self):
        print("\n=== PEDIDOS POR FECHA ===")
        fecha_str = input("Fecha (dd/mm/aaaa): ")
        
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        except ValueError:
            print("❌ Formato de fecha inválido. Usa dd/mm/aaaa")
            return
        
        pedidos = self.pedido_service.obtener_pedidos_por_fecha(fecha)
        
        if not pedidos:
            print(f"📭 No hay pedidos para la fecha {fecha_str}.")
            return
        
        print(f"\n📦 PEDIDOS DEL {fecha_str}:")
        for pedido in pedidos:
            cliente = self.cliente_service.obtener_cliente(pedido.id_cliente)
            nombre_cliente = cliente.nombre if cliente else "No encontrado"
            estado_icon = "🟡" if pedido.estado == "Pendiente" else "🟢" if pedido.estado == "Entregado" else "🔴"
            print(f"   {estado_icon} {pedido.id_pedido}: {nombre_cliente} - ${pedido.total} - {pedido.estado}")