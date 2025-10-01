from managers.producto_manager import ProductoManager
from managers.cliente_manager import ClienteManager
from managers.pedido_manager import PedidoManager
from managers.comunicacion_manager import ComunicacionManager

class TiendaVirtual:
    def __init__(self):
        self.producto_manager = ProductoManager()
        self.cliente_manager = ClienteManager()
        self.pedido_manager = PedidoManager()
        self.comunicacion_manager = ComunicacionManager()
    
    def mostrar_menu_principal(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_titulo_bonito("🛍️ TIENDA VIRTUAL 🛍️")
            print(" ───────────────────────────────────────────────── ")
            print("│    1. 📦 Gestión de Productos                   │")
            print("│    2. 👥 Gestión de Clientes                    │")
            print("│    3. 📋 Gestión de Pedidos                     │")
            print("│    4. 📞 Comunicación con Clientes              │")
            print("│    5. 🚪 Salir                                  │")
            print(" ─────────────────────────────────────────────────")
            
            opcion = input("\n👉 Selecciona una opción (1-5): ")
            
            if opcion == "1":
                self.menu_gestion_productos()
            elif opcion == "2":
                self.menu_gestion_clientes()
            elif opcion == "3":
                self.menu_gestion_pedidos()
            elif opcion == "4":
                self.menu_comunicacion()
            elif opcion == "5":
                print("   ¡Gracias por usar la Tienda Virtual! 👋")
                break
            else:
                print("\n❌ Opción inválida. Intenta nuevamente.")
                self._pausar()
    
    def menu_gestion_productos(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_titulo_bonito("📦 GESTIÓN DE PRODUCTOS")
            print(" ────────────────────────────────────────────")
            print("│  1. 🆕 Registrar nuevo producto            │")
            print("│  2. 👀 Ver catálogo de productos           │")
            print("│  3. 🔍 Buscar producto por ID / nombre     │")
            print("│  4. ✏️ Actualizar información de producto  │")
            print("│  5. 🗑️ Eliminar producto                   │")
            print("│  6. ⚠️ Ver productos con stock bajo        │")
            print("│  7. ↩️ Volver al menú principal            │ ")
            print(" ──────────────────────────────────────────── ")
            
            opcion = input("\n👉 Selecciona una opción (1-7): ")
            
            if opcion == "1":
                self.producto_manager.registrar_producto()
            elif opcion == "2":
                self.producto_manager.ver_catalogo()
            elif opcion == "3":
                self.producto_manager.buscar_producto()
            elif opcion == "4":
                self.producto_manager.actualizar_producto()
            elif opcion == "5":
                self.producto_manager.eliminar_producto()
            elif opcion == "6":
                self.producto_manager.ver_stock_bajo()
            elif opcion == "7":
                break
            else:
                print("\n❌ Opción inválida.")
            
            self._pausar()
    
    def menu_gestion_clientes(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_titulo_bonito("👥 GESTIÓN DE CLIENTES")
            
            print(" ────────────────────────────────────────────")
            print("│  1. 🆕 Registrar nuevo cliente             │")
            print("│  2. 👀 Ver lista de clientes               │")
            print("│  3. 🔍 Buscar cliente por ID / nombre      │")
            print("│  4. ✏️ Actualizar datos del cliente        │")
            print("│  5. 🗑️ Eliminar cliente                    │")
            print("│  6. 🏢 Filtrar clientes por tipo           │")
            print("│  7. ↩️ Volver al menú principal            │")
            print(" ──────────────────────────────────────────── ")
            
            opcion = input("\n👉 Selecciona una opción (1-7): ")
            
            if opcion == "1":
                self.cliente_manager.registrar_cliente()
            elif opcion == "2":
                self.cliente_manager.ver_clientes()
            elif opcion == "3":
                self.cliente_manager.buscar_cliente()
            elif opcion == "4":
                self.cliente_manager.actualizar_cliente()
            elif opcion == "5":
                self.cliente_manager.eliminar_cliente()
            elif opcion == "6":
                self.cliente_manager.filtrar_por_tipo()
            elif opcion == "7":
                break
            else:
                print("\n❌ Opción inválida.")
            
            self._pausar()
    
    def menu_gestion_pedidos(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_titulo_bonito("📋 GESTIÓN DE PEDIDOS")
            print(" ────────────────────────────────────────────")
            print("│  1. 🆕 Registrar nuevo pedido              │")
            print("│  2. 👀 Ver pedidos registrados             │")
            print("│  3. 🔍 Buscar pedido por ID                │")
            print("│  4. 📊 Actualizar estado del pedido        │")
            print("│  5. ❌ Cancelar pedido                     │")
            print("│  6. 👤 Ver pedidos por cliente             │")
            print("│  7. 📅 Ver pedidos por fecha               │")
            print("│  8. ↩️ Volver al menú principal            │")
            print(" ────────────────────────────────────────────")
            
            opcion = input("\n👉 Selecciona una opción (1-8): ")
            
            if opcion == "1":
                self.pedido_manager.registrar_pedido()
            elif opcion == "2":
                self.pedido_manager.ver_pedidos()
            elif opcion == "3":
                self.pedido_manager.buscar_pedido()
            elif opcion == "4":
                self.pedido_manager.actualizar_estado()
            elif opcion == "5":
                self.pedido_manager.cancelar_pedido()
            elif opcion == "6":
                self.pedido_manager.ver_pedidos_cliente()
            elif opcion == "7":
                self.pedido_manager.ver_pedidos_fecha()
            elif opcion == "8":
                break
            else:
                print("\n❌ Opción inválida.")
            
            self._pausar()
    
    def menu_comunicacion(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_titulo_bonito("📞 COMUNICACIÓN CON CLIENTES")
            
            print(" ────────────────────────────────────────────")
            print("│  1. 📱 Enviar mensaje por WhatsApp         │")
            print("│  2. 📧 Enviar correo electrónico           │")
            print("│  3. 📜 Ver historial de comunicaciones     │")
            print("│  4. ↩️ Volver al menú principal            │")
            print(" ────────────────────────────────────────────")
            
            opcion = input("\n👉 Selecciona una opción (1-4): ")
            
            if opcion == "1":
                self.comunicacion_manager.enviar_whatsapp()
            elif opcion == "2":
                self.comunicacion_manager.enviar_email()
            elif opcion == "3":
                self.comunicacion_manager.ver_historial()
            elif opcion == "4":
                break
            else:
                print("\n❌ Opción inválida.")
            
            self._pausar()
    
    def _limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _pausar(self):
        """Pausa la ejecución hasta que el usuario presione Enter"""
        input("\n↵ Presiona Enter para continuar...")
    
    def _mostrar_titulo_bonito(self, titulo):
        """Muestra un título formateado con bordes"""
        ancho = 50
        print("\n" + "╔" + "═" * (ancho - 2) + "╗")
        print("║" + titulo.center(ancho - 2) + "")
        print("╚" + "═" * (ancho - 2) + "╝")

if __name__ == "__main__":
    tienda = TiendaVirtual()
    tienda.mostrar_menu_principal()