from services.cliente_service import ClienteService
from models.cliente import Cliente

class ClienteManager:
    def __init__(self):
        self.cliente_service = ClienteService()
    
    def registrar_cliente(self):
        print("\n=== REGISTRAR NUEVO CLIENTE ===")
        
        id_cliente = input("ID cliente: ")
        nombre = input("Nombre completo: ")
        celular = input("Celular: ")
        direccion = input("Dirección: ")
        ciudad = input("Ciudad: ")
        email = input("Correo electrónico: ")
        
        print("\n🏢 TIPO DE CLIENTE:")
        print("  1. Mayorista")
        print("  2. Minorista")
        tipo_opcion = input("Selecciona tipo (1-2): ")
        tipo_cliente = "Mayorista" if tipo_opcion == "1" else "Minorista"
        
        cliente = Cliente(id_cliente, nombre, celular, direccion, ciudad, email, tipo_cliente)
        success, message = self.cliente_service.registrar_cliente(cliente)
        
        print(f"\n{'✅' if success else '❌'} {message}")
    
    def ver_clientes(self):
        print("\n=== LISTA DE CLIENTES ===")
        clientes = self.cliente_service.obtener_todos_clientes()
        
        if not clientes:
            print("No hay clientes registrados.")
            return
        
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'TIPO':<12} {'CIUDAD':<15} {'CELULAR':<12}")
        print("=" * 80)
        
        for cliente in clientes:
            tipo_icon = "🏢" if cliente.tipo_cliente == "Mayorista" else "👤"
            print(f"{cliente.id_cliente:<10} {cliente.nombre:<25} {tipo_icon} {cliente.tipo_cliente:<10} {cliente.ciudad:<15} {cliente.celular:<12}")
    
    def buscar_cliente(self):
        print("\n=== BUSCAR CLIENTE ===")
        criterio = input("Buscar por ID o nombre: ")
        
        cliente = self.cliente_service.obtener_cliente(criterio)
        if cliente:
            print(f"\n✅ CLIENTE ENCONTRADO:")
            print(f"   ID: {cliente.id_cliente}")
            print(f"   Nombre: {cliente.nombre}")
            print(f"   Celular: {cliente.celular}")
            print(f"   Dirección: {cliente.direccion}")
            print(f"   Ciudad: {cliente.ciudad}")
            print(f"   Email: {cliente.email}")
            print(f"   Tipo: {cliente.tipo_cliente}")
            return
        
        clientes = self.cliente_service.buscar_clientes_por_nombre(criterio)
        if clientes:
            print(f"\n🔍 Se encontraron {len(clientes)} clientes:")
            for cliente in clientes:
                tipo_icon = "🏢" if cliente.tipo_cliente == "Mayorista" else "👤"
                print(f"   {tipo_icon} {cliente}")
        else:
            print("❌ No se encontraron clientes.")
    
    def actualizar_cliente(self):
        print("\n=== ACTUALIZAR CLIENTE ===")
        id_cliente = input("ID del cliente a actualizar: ")
        
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        print(f"\nCliente actual: {cliente}")
        print("\nDeja en blanco los campos que no quieras cambiar:")
        
        nuevos_datos = {}
        nombre = input(f"Nuevo nombre [{cliente.nombre}]: ")
        if nombre: nuevos_datos['nombre'] = nombre
        
        celular = input(f"Nuevo celular [{cliente.celular}]: ")
        if celular: nuevos_datos['celular'] = celular
        
        direccion = input(f"Nueva dirección [{cliente.direccion}]: ")
        if direccion: nuevos_datos['direccion'] = direccion
        
        ciudad = input(f"Nueva ciudad [{cliente.ciudad}]: ")
        if ciudad: nuevos_datos['ciudad'] = ciudad
        
        email = input(f"Nuevo email [{cliente.email}]: ")
        if email: nuevos_datos['email'] = email
        
        tipo_cliente = input(f"Nuevo tipo [{cliente.tipo_cliente}]: ")
        if tipo_cliente: nuevos_datos['tipo_cliente'] = tipo_cliente
        
        if nuevos_datos:
            success, message = self.cliente_service.actualizar_cliente(id_cliente, nuevos_datos)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ No se realizaron cambios.")
    
    def eliminar_cliente(self):
        print("\n=== ELIMINAR CLIENTE ===")
        id_cliente = input("ID del cliente a eliminar: ")
        
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        confirmacion = input(f"¿Estás seguro de eliminar {cliente.nombre}? (s/n): ")
        if confirmacion.lower() == 's':
            success, message = self.cliente_service.eliminar_cliente(id_cliente)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ Eliminación cancelada.")
    
    def filtrar_por_tipo(self):
        print("\n=== FILTRAR CLIENTES POR TIPO ===")
        print("  1. Mayorista")
        print("  2. Minorista")
        tipo_opcion = input("Selecciona tipo a filtrar (1-2): ")
        tipo_cliente = "Mayorista" if tipo_opcion == "1" else "Minorista"
        
        clientes = self.cliente_service.filtrar_clientes_por_tipo(tipo_cliente)
        
        if not clientes:
            print(f"❌ No hay clientes del tipo {tipo_cliente}.")
            return
        
        print(f"\n👥 CLIENTES {tipo_cliente.upper()}:")
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'CIUDAD':<15} {'CELULAR':<12}")
        print("=" * 65)
        
        for cliente in clientes:
            print(f"{cliente.id_cliente:<10} {cliente.nombre:<25} {cliente.ciudad:<15} {cliente.celular:<12}")