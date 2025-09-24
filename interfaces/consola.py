from managers.cliente_manager import manager_clientes
from managers.pedido_manager import manager_pedidos
from models.cliente import Cliente
from models.pedido import Pedido

class InterfazConsola:
    def __init__(self):
        self.manager_clientes = manager_clientes
        self.manager_pedidos = manager_pedidos
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal de la aplicación"""
        while True:
            print("\n" + "="*50)
            print("🏪 TIENDA VIRTUAL - SISTEMA DE GESTIÓN")
            print("="*50)
            print("1. 👥 Gestión de Clientes")
            print("2. 📦 Gestión de Pedidos")
            print("3. 📊 Reportes y Estadísticas")
            print("4. 🚪 Salir")
            print("="*50)
            
            opcion = input("Seleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                self.menu_gestion_clientes()
            elif opcion == "2":
                self.menu_gestion_pedidos()
            elif opcion == "3":
                self.menu_reportes()
            elif opcion == "4":
                print("¡Gracias por usar el sistema de Tienda Virtual! 👋")
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-4.")
    
    def menu_gestion_clientes(self):
        """Menú de gestión de clientes"""
        while True:
            print("\n" + "="*40)
            print("👥 GESTIÓN DE CLIENTES")
            print("="*40)
            print("1. 📋 Listar todos los clientes")
            print("2. ➕ Agregar nuevo cliente")
            print("3. 🔍 Buscar cliente")
            print("4. ✏️ Editar cliente")
            print("5. 🚫 Desactivar cliente")
            print("6. ✅ Reactivar cliente")
            print("7. 📊 Estadísticas de clientes")
            print("8. ↩️ Volver al menú principal")
            print("="*40)
            
            opcion = input("Seleccione una opción (1-8): ").strip()
            
            if opcion == "1":
                self.listar_clientes()
            elif opcion == "2":
                self.agregar_cliente()
            elif opcion == "3":
                self.buscar_cliente()
            elif opcion == "4":
                self.editar_cliente()
            elif opcion == "5":
                self.desactivar_cliente()
            elif opcion == "6":
                self.activar_cliente()
            elif opcion == "7":
                self.mostrar_estadisticas_clientes()
            elif opcion == "8":
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-8.")
    
    def menu_gestion_pedidos(self):
        """Menú de gestión de pedidos"""
        while True:
            print("\n" + "="*40)
            print("📦 GESTIÓN DE PEDIDOS")
            print("="*40)
            print("1. 📋 Listar todos los pedidos")
            print("2. ➕ Crear nuevo pedido")
            print("3. 🔍 Buscar pedido por ID")
            print("4. 👤 Ver pedidos de un cliente")
            print("5. ✏️ Cambiar estado de pedido")
            print("6. 🛒 Agregar producto a pedido")
            print("7. 🗑️ Eliminar producto de pedido")
            print("8. 💰 Aplicar descuento a pedido")
            print("9. 🚫 Cancelar pedido")
            print("10. ↩️ Volver al menú principal")
            print("="*40)
            
            opcion = input("Seleccione una opción (1-10): ").strip()
            
            if opcion == "1":
                self.listar_pedidos()
            elif opcion == "2":
                self.crear_pedido()
            elif opcion == "3":
                self.buscar_pedido()
            elif opcion == "4":
                self.pedidos_por_cliente()
            elif opcion == "5":
                self.cambiar_estado_pedido()
            elif opcion == "6":
                self.agregar_producto_pedido()
            elif opcion == "7":
                self.eliminar_producto_pedido()
            elif opcion == "8":
                self.aplicar_descuento_pedido()
            elif opcion == "9":
                self.cancelar_pedido()
            elif opcion == "10":
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-10.")
    
    def menu_reportes(self):
        """Menú de reportes y estadísticas"""
        while True:
            print("\n" + "="*40)
            print("📊 REPORTES Y ESTADÍSTICAS")
            print("="*40)
            print("1. 📈 Estadísticas generales")
            print("2. 👥 Reporte de clientes")
            print("3. 📦 Reporte de pedidos")
            print("4. 💰 Ventas por estado")
            print("5. ↩️ Volver al menú principal")
            print("="*40)
            
            opcion = input("Seleccione una opción (1-5): ").strip()
            
            if opcion == "1":
                self.estadisticas_generales()
            elif opcion == "2":
                self.reporte_clientes()
            elif opcion == "3":
                self.reporte_pedidos()
            elif opcion == "4":
                self.ventas_por_estado()
            elif opcion == "5":
                break
            else:
                print("❌ Opción inválida. Por favor, seleccione 1-5.")
    
    # ========== MÉTODOS DE CLIENTES ==========
    
    def listar_clientes(self):
        """Lista todos los clientes"""
        print("\n📋 LISTA DE CLIENTES ACTIVOS:")
        clientes = self.manager_clientes.listar_clientes()
        
        if not clientes:
            print("No hay clientes activos.")
            return
        
        for i, cliente in enumerate(clientes, 1):
            print(f"\n{i}. {cliente.nombre} (ID: {cliente.id})")
            print(f"   📧 {cliente.email}")
            print(f"   📍 {cliente.direccion}")
            print(f"   📞 {cliente.telefono if cliente.telefono else 'No registrado'}")
            print(f"   🛒 Pedidos: {len(cliente.pedidos)}")
            print("-" * 30)
    
    def agregar_cliente(self):
        """Agrega un nuevo cliente"""
        print("\n➕ AGREGAR NUEVO CLIENTE:")
        
        nombre = input("Nombre completo: ").strip()
        email = input("Email: ").strip()
        direccion = input("Dirección: ").strip()
        telefono = input("Teléfono (opcional): ").strip()
        
        if not nombre or not email or not direccion:
            print("❌ Error: Nombre, email y dirección son obligatorios.")
            return
        
        try:
            cliente = self.manager_clientes.agregar_cliente(nombre, email, direccion, telefono)
            print(f"✅ Cliente agregado exitosamente:")
            print(f"   ID: {cliente.id}")
            print(f"   Nombre: {cliente.nombre}")
            print(f"   Email: {cliente.email}")
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    def buscar_cliente(self):
        """Busca un cliente por diferentes criterios"""
        print("\n🔍 BUSCAR CLIENTE:")
        print("1. Por ID")
        print("2. Por nombre")
        print("3. Por email")
        
        opcion = input("Seleccione tipo de búsqueda (1-3): ").strip()
        
        if opcion == "1":
            try:
                id_cliente = int(input("ID del cliente: "))
                cliente = self.manager_clientes.buscar_por_id(id_cliente)
                if cliente:
                    print(cliente.obtener_info())
                else:
                    print("❌ Cliente no encontrado.")
            except ValueError:
                print("❌ ID debe ser un número.")
        
        elif opcion == "2":
            nombre = input("Nombre a buscar: ").strip()
            resultados = self.manager_clientes.buscar_por_nombre(nombre)
            if resultados:
                for cliente in resultados:
                    print(cliente.obtener_info())
            else:
                print("❌ No se encontraron clientes con ese nombre.")
        
        elif opcion == "3":
            email = input("Email a buscar: ").strip()
            cliente = self.manager_clientes.buscar_por_email(email)
            if cliente:
                print(cliente.obtener_info())
            else:
                print("❌ Cliente no encontrado.")
        else:
            print("❌ Opción inválida.")
    
    # ========== MÉTODOS DE PEDIDOS ==========
    
    def listar_pedidos(self):
        """Lista todos los pedidos"""
        print("\n📦 LISTA DE PEDIDOS:")
        pedidos = self.manager_pedidos.listar_pedidos()
        
        if not pedidos:
            print("No hay pedidos registrados.")
            return
        
        for pedido in pedidos:
            cliente = self.manager_clientes.buscar_por_id(pedido.cliente_id)
            nombre_cliente = cliente.nombre if cliente else "Cliente no encontrado"
            
            print(f"\n🛒 Pedido #{pedido.id} - Cliente: {nombre_cliente}")
            print(f"   📅 Fecha: {pedido.fecha}")
            print(f"   💰 Total: ${pedido.total:.2f}")
            print(f"   📊 Estado: {pedido.estado.upper()}")
            print(f"   📦 Productos: {len(pedido.productos)}")
            print("-" * 40)
    
    def crear_pedido(self):
        """Crea un nuevo pedido"""
        print("\n➕ CREAR NUEVO PEDIDO:")
        
        # Listar clientes activos
        clientes = self.manager_clientes.listar_clientes()
        if not clientes:
            print("❌ No hay clientes activos para crear pedidos.")
            return
        
        print("Clientes activos:")
        for cliente in clientes:
            print(f"ID: {cliente.id} - {cliente.nombre}")
        
        try:
            cliente_id = int(input("\nID del cliente: "))
            
            # Verificar que el cliente existe
            cliente = self.manager_clientes.buscar_por_id(cliente_id)
            if not cliente or not cliente.activo:
                print("❌ Cliente no encontrado o inactivo.")
                return
            
            pedido = self.manager_pedidos.crear_pedido(cliente_id)
            print(f"✅ Pedido creado exitosamente: #{pedido.id}")
            
            # Preguntar si quiere agregar productos inmediatamente
            agregar_productos = input("¿Agregar productos ahora? (s/n): ").strip().lower()
            if agregar_productos == 's':
                self.agregar_productos_interactivo(pedido.id)
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def agregar_productos_interactivo(self, pedido_id):
        """Agrega productos a un pedido de forma interactiva"""
        print("\n🛒 AGREGAR PRODUCTOS AL PEDIDO:")
        
        while True:
            producto = input("Nombre del producto (o 'fin' para terminar): ").strip()
            if producto.lower() == 'fin':
                break
            
            try:
                precio = float(input("Precio del producto: $"))
                resultado = self.manager_pedidos.agregar_producto_pedido(pedido_id, producto, precio)
                print(f"✅ {resultado}")
            except ValueError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Error: {e}")
    
    # ========== MÉTODOS DE REPORTES ==========
    
    def estadisticas_generales(self):
        """Muestra estadísticas generales"""
        print("\n📊 ESTADÍSTICAS GENERALES:")
        
        stats_clientes = self.manager_clientes.obtener_estadisticas()
        stats_pedidos = self.manager_pedidos.obtener_estadisticas()
        
        print("\n👥 ESTADÍSTICAS DE CLIENTES:")
        print(f"   Total de clientes: {stats_clientes['total_clientes']}")
        print(f"   Clientes activos: {stats_clientes['clientes_activos']}")
        print(f"   Clientes inactivos: {stats_clientes['clientes_inactivos']}")
        print(f"   Clientes con pedidos: {stats_clientes['clientes_con_pedidos']}")
        print(f"   Total de pedidos: {stats_clientes['total_pedidos']}")
        print(f"   Promedio de pedidos por cliente: {stats_clientes['promedio_pedidos_por_cliente']:.1f}")
        
        print("\n📦 ESTADÍSTICAS DE PEDIDOS:")
        print(f"   Total de pedidos: {stats_pedidos['total_pedidos']}")
        print(f"   Ventas totales: ${stats_pedidos['total_ventas']:.2f}")
        print(f"   Venta promedio: ${stats_pedidos['venta_promedio']:.2f}")
        print(f"   Pedido de mayor valor: #{stats_pedidos['pedido_mayor_valor']} (${stats_pedidos['valor_mayor_pedido']:.2f})")
        
        print("\n📊 PEDIDOS POR ESTADO:")
        for estado, cantidad in stats_pedidos['pedidos_por_estado'].items():
            print(f"   {estado}: {cantidad} pedidos")
    
    def ventas_por_estado(self):
        """Muestra ventas totales por estado de pedido"""
        print("\n💰 VENTAS POR ESTADO DE PEDIDO:")
        
        pedidos = self.manager_pedidos.listar_pedidos()
        ventas_por_estado = {}
        
        for pedido in pedidos:
            estado = pedido.estado
            if estado not in ventas_por_estado:
                ventas_por_estado[estado] = 0
            ventas_por_estado[estado] += pedido.total
        
        for estado, total in ventas_por_estado.items():
            print(f"   {estado.upper()}: ${total:.2f}")
    
    # (Aquí irían los demás métodos similares...)
    
    def iniciar(self):
        """Inicia la aplicación"""
        print("🚀 Iniciando Tienda Virtual...")
        print("✅ Sistema cargado correctamente")
        
        # Mostrar resumen inicial
        stats_clientes = self.manager_clientes.obtener_estadisticas()
        stats_pedidos = self.manager_pedidos.obtener_estadisticas()
        
        print(f"\n📊 RESUMEN INICIAL:")
        print(f"   👥 Clientes: {stats_clientes['clientes_activos']} activos")
        print(f"   📦 Pedidos: {stats_pedidos['total_pedidos']} totales")
        print(f"   💰 Ventas: ${stats_pedidos['total_ventas']:.2f}")
        
        input("\nPresione Enter para continuar...")
        self.mostrar_menu_principal()

# Métodos restantes (editar_cliente, desactivar_cliente, etc.) seguirían el mismo patrón
# Por brevedad, los he simplificado pero la estructura es similar

if __name__ == "__main__":
    app = InterfazConsola()
    app.iniciar()