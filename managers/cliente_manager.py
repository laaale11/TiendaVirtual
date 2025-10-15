from services.cliente_service import ClienteService
from models.cliente import Cliente
from utils.validadores import *

class ClienteManager:
    def __init__(self):
        self.cliente_service = ClienteService()
    
    def _mostrar_titulo(self, titulo):
        print(f"\n╔{'═' * 50}╗")
        print(f"║{titulo:^50}")
        print(f"╚{'═' * 50}╝")
    
    def _solicitar_dato(self, mensaje, validador, mensaje_error):
        """Solicita un dato hasta que sea válido"""
        while True:
            try:
                dato = input(mensaje)
                if validador(dato):
                    return dato
                else:
                    print(f"❌ {mensaje_error}")
            except KeyboardInterrupt:
                print("\n\n⚠️ Operación cancelada por el usuario")
                return None

    def registrar_cliente(self):
        self._mostrar_titulo("🆕 REGISTRAR CLIENTE")
        
        try:
            # Solicitar datos con validación
            id_cliente = self._solicitar_dato(
                "📋 ID cliente: ", 
                validar_texto, 
                "El ID no puede estar vacío"
            )
            if id_cliente is None: return
            
            nombre = self._solicitar_dato(
                "👤 Nombre completo: ", 
                validar_texto, 
                "El nombre no puede estar vacío"
            )
            if nombre is None: return
            
            celular = self._solicitar_dato(
                "📞 Celular: ", 
                validar_telefono, 
                "El celular debe contener solo números (7-15 dígitos)"
            )
            if celular is None: return
            
            direccion = input("🏠 Dirección: ") or "Sin dirección"
            ciudad = input("🏙️ Ciudad: ") or "Sin ciudad"
            
            email = self._solicitar_dato(
                "📧 Correo electrónico: ", 
                validar_email, 
                "El email no tiene un formato válido"
            )
            if email is None: return
            
            # Tipo de cliente con menú validado
            print("\n🏢 TIPO DE CLIENTE:")
            print("  1. Mayorista")
            print("  2. Minorista")
            
            tipo_opcion = self._solicitar_dato(
                "👉 Selecciona tipo (1-2): ",
                lambda x: validar_opcion_menu(x, 2),
                "Selecciona 1 para Mayorista o 2 para Minorista"
            )
            if tipo_opcion is None: return
            
            tipo_cliente = "Mayorista" if tipo_opcion == "1" else "Minorista"
            
            # Crear y guardar cliente
            cliente = Cliente(id_cliente, nombre, celular, direccion, ciudad, email, tipo_cliente)
            success, message = self.cliente_service.registrar_cliente(cliente)
            
            print(f"\n{'✅' if success else '❌'} {message}")
            
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    def ver_clientes(self):
        self._mostrar_titulo("👥 LISTA DE CLIENTES")
        clientes = self.cliente_service.obtener_todos_clientes()
        
        if not clientes:
            print("📭 No hay clientes registrados.")
            return
        
        # Mostrar solo clientes activos
        clientes_activos = [c for c in clientes if c.activo]
        
        if not clientes_activos:
            print("📭 No hay clientes activos.")
            return
        
        print(f"\nMostrando {len(clientes_activos)} clientes activos:")
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'TIPO':<12} {'CIUDAD':<15} {'ESTADO':<8}")
        print("=" * 75)
        
        for cliente in clientes_activos:
            tipo_icon = "🏢" if cliente.tipo_cliente == "Mayorista" else "👤"
            estado = "ACTIVO" if cliente.activo else "INACTIVO"
            print(f"{cliente.id_cliente:<10} {cliente.nombre:<25} {tipo_icon} {cliente.tipo_cliente:<10} {cliente.ciudad:<15} {estado:<8}")

    def buscar_cliente(self):
        self._mostrar_titulo("🔍 BUSCAR CLIENTE")
        criterio = input("👉 Buscar por ID o nombre: ")
        
        if not criterio.strip():
            print("❌ El criterio de búsqueda no puede estar vacío")
            return
        
        cliente = self.cliente_service.obtener_cliente(criterio)
        if cliente:
            estado = "✅ ACTIVO" if cliente.activo else "❌ INACTIVO"
            print(f"\n✅ CLIENTE ENCONTRADO:")
            print(f"┌{'─' * 40}┐")
            print(f"│ 📋 ID: {cliente.id_cliente:<28} {estado} │")
            print(f"│ 👤 Nombre: {cliente.nombre:<26} │")
            print(f"│ 📞 Celular: {cliente.celular:<25} │")
            print(f"│ 🏠 Dirección: {cliente.direccion:<23} │")
            print(f"│ 🏙️ Ciudad: {cliente.ciudad:<26} │")
            print(f"│ 📧 Email: {cliente.email:<26} │")
            print(f"│ 🏢 Tipo: {cliente.tipo_cliente:<27} │")
            print(f"└{'─' * 40}┘")
            return
        
        clientes = self.cliente_service.buscar_clientes_por_nombre(criterio)
        clientes_activos = [c for c in clientes if c.activo]
        
        if clientes_activos:
            print(f"\n🔍 Se encontraron {len(clientes_activos)} clientes activos:")
            for cliente in clientes_activos:
                tipo_icon = "🏢" if cliente.tipo_cliente == "Mayorista" else "👤"
                print(f"   {tipo_icon} {cliente}")
        else:
            print("❌ No se encontraron clientes activos.")

    def actualizar_cliente(self):
        self._mostrar_titulo("✏️ ACTUALIZAR CLIENTE")
        id_cliente = input("👉 ID del cliente a actualizar: ")
        
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        print(f"\n👤 Cliente actual: {cliente}")
        print("\n💡 Deja en blanco los campos que no quieras cambiar:")
        
        nuevos_datos = {}
        
        nombre = input(f"👤 Nuevo nombre [{cliente.nombre}]: ")
        if nombre and validar_texto(nombre):
            nuevos_datos['nombre'] = nombre
        
        celular = input(f"📞 Nuevo celular [{cliente.celular}]: ")
        if celular and validar_telefono(celular):
            nuevos_datos['celular'] = celular
        
        direccion = input(f"🏠 Nueva dirección [{cliente.direccion}]: ")
        if direccion:
            nuevos_datos['direccion'] = direccion
        
        ciudad = input(f"🏙️ Nueva ciudad [{cliente.ciudad}]: ")
        if ciudad:
            nuevos_datos['ciudad'] = ciudad
        
        email = input(f"📧 Nuevo email [{cliente.email}]: ")
        if email and validar_email(email):
            nuevos_datos['email'] = email
        
        if nuevos_datos:
            success, message = self.cliente_service.actualizar_cliente(id_cliente, nuevos_datos)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ No se realizaron cambios.")

    def cambiar_estado_cliente(self):
        self._mostrar_titulo("🔄 CAMBIAR ESTADO DE CLIENTE")
        id_cliente = input("👉 ID del cliente: ")
        
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        estado_actual = "ACTIVO" if cliente.activo else "INACTIVO"
        print(f"\n👤 Cliente: {cliente.nombre}")
        print(f"📊 Estado actual: {estado_actual}")
        
        print("\n🔄 OPCIONES:")
        print("1. ✅ Activar cliente")
        print("2. ❌ Desactivar cliente")
        print("3. ↩️ Cancelar")
        
        opcion = input("\n👉 Selecciona una opción (1-3): ")
        
        if opcion == "1":
            if cliente.activo:
                print("❌ El cliente ya está activo.")
            else:
                success, message = self.cliente_service.actualizar_cliente(id_cliente, {'activo': True})
                print(f"\n{'✅' if success else '❌'} {message}")
        
        elif opcion == "2":
            if not cliente.activo:
                print("❌ El cliente ya está inactivo.")
            else:
                success, message = self.cliente_service.actualizar_cliente(id_cliente, {'activo': False})
                print(f"\n{'✅' if success else '❌'} {message}")
        
        elif opcion == "3":
            print("✅ Operación cancelada.")
        
        else:
            print("❌ Opción inválida.")

    def filtrar_por_tipo(self):
        self._mostrar_titulo("🏢 FILTRAR CLIENTES POR TIPO")
        print("  1. Mayorista")
        print("  2. Minorista")
        
        tipo_opcion = self._solicitar_dato(
            "👉 Selecciona tipo a filtrar (1-2): ",
            lambda x: validar_opcion_menu(x, 2),
            "Selecciona 1 para Mayorista o 2 para Minorista"
        )
        if tipo_opcion is None: return
        
        tipo_cliente = "Mayorista" if tipo_opcion == "1" else "Minorista"
        
        clientes = self.cliente_service.filtrar_clientes_por_tipo(tipo_cliente)
        clientes_activos = [c for c in clientes if c.activo]
        
        if not clientes_activos:
            print(f"📭 No hay clientes {tipo_cliente} activos.")
            return
        
        print(f"\n👥 CLIENTES {tipo_cliente.upper()} ACTIVOS:")
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'CIUDAD':<15} {'CELULAR':<12}")
        print("=" * 65)
        
        for cliente in clientes_activos:
            print(f"{cliente.id_cliente:<10} {cliente.nombre:<25} {cliente.ciudad:<15} {cliente.celular:<12}")