from services.producto_service import ProductoService
from models.producto import Producto
from utils.validadores import *

class ProductoManager:
    def __init__(self):
        self.producto_service = ProductoService()
    
    def _mostrar_titulo(self, titulo):
        print(f"\n╔{'═' * 50}╗")
        print(f"║{titulo:^50}║")
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
    
    def registrar_producto(self):
        self._mostrar_titulo("🆕 REGISTRAR PRODUCTO")
        
        try:
            # Solicitar datos con validación
            id_producto = self._solicitar_dato(
                "📋 ID producto: ", 
                validar_texto, 
                "El ID no puede estar vacío"
            )
            if id_producto is None: return
            
            nombre = self._solicitar_dato(
                "📦 Nombre: ", 
                validar_texto, 
                "El nombre no puede estar vacío"
            )
            if nombre is None: return
            
            descripcion = input("📝 Descripción: ") or "Sin descripción"
            
            # Precios con validación
            print("\n💲 PRECIOS:")
            precio_unidad_str = self._solicitar_dato(
                "💰 Precio por unidad: $", 
                validar_precio, 
                "El precio debe ser un número positivo"
            )
            if precio_unidad_str is None: return
            precio_unidad = float(precio_unidad_str)
            
            precio_docena_str = self._solicitar_dato(
                "💰 Precio por docena: $", 
                validar_precio, 
                "El precio debe ser un número positivo"
            )
            if precio_docena_str is None: return
            precio_docena = float(precio_docena_str)
            
            precio_caja_str = self._solicitar_dato(
                "💰 Precio por caja: $", 
                validar_precio, 
                "El precio debe ser un número positivo"
            )
            if precio_caja_str is None: return
            precio_caja = float(precio_caja_str)
            
            # Stock con validación
            stock_str = self._solicitar_dato(
                "📊 Stock disponible: ", 
                validar_entero_positivo, 
                "El stock debe ser un número entero positivo"
            )
            if stock_str is None: return
            stock = int(stock_str)
            
            # Categoría con menú validado
            print("\n📁 CATEGORÍAS:")
            for i, categoria in enumerate(Producto.CATEGORIAS_PERMITIDAS, 1):
                print(f"  {i}. {categoria.title()}")
            
            categoria_opcion = self._solicitar_dato(
                f"\n👉 Selecciona categoría (1-{len(Producto.CATEGORIAS_PERMITIDAS)}): ",
                lambda x: validar_opcion_menu(x, len(Producto.CATEGORIAS_PERMITIDAS)),
                f"Selecciona un número entre 1 y {len(Producto.CATEGORIAS_PERMITIDAS)}"
            )
            if categoria_opcion is None: return
            
            categoria_index = int(categoria_opcion) - 1
            categoria = Producto.CATEGORIAS_PERMITIDAS[categoria_index]
            
            # Stock mínimo
            stock_minimo_str = input("⚠️  Stock mínimo (default 10): ") or "10"
            if not validar_entero_positivo(stock_minimo_str):
                print("❌ Stock mínimo inválido, usando valor por defecto: 10")
                stock_minimo = 10
            else:
                stock_minimo = int(stock_minimo_str)
            
            # Crear y guardar producto
            producto = Producto(id_producto, nombre, descripcion, precio_unidad, precio_docena, precio_caja, stock, categoria, stock_minimo)
            success, message = self.producto_service.registrar_producto(producto)
            
            print(f"\n{'✅' if success else '❌'} {message}")
            
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def ver_catalogo(self):
        self._mostrar_titulo("📦 CATÁLOGO DE PRODUCTOS")
        productos = self.producto_service.obtener_todos_productos()
        
        if not productos:
            print("📭 No hay productos registrados.")
            return
        
        # Mostrar solo productos activos
        productos_activos = [p for p in productos if p.activo]
        
        if not productos_activos:
            print("📭 No hay productos activos en el catálogo.")
            return
        
        print(f"\nMostrando {len(productos_activos)} productos activos:")
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'PRECIO UNI':<12} {'STOCK':<8} {'ESTADO':<8}")
        print("=" * 70)
        
        for producto in productos_activos:
            stock_icon = "⚠️" if producto.tiene_stock_bajo() else "✅"
            estado = "ACTIVO" if producto.activo else "INACTIVO"
            print(f"{producto.id_producto:<10} {producto.nombre:<25} ${producto.precio_unidad:<11} {stock_icon} {producto.stock:<6} {estado:<8}")
    
    def buscar_producto(self):
        self._mostrar_titulo("🔍 BUSCAR PRODUCTO")
        criterio = input("👉 Buscar por ID o nombre: ")
        
        if not criterio.strip():
            print("❌ El criterio de búsqueda no puede estar vacío")
            return
        
        producto = self.producto_service.obtener_producto(criterio)
        if producto:
            estado = "✅ ACTIVO" if producto.activo else "❌ INACTIVO"
            print(f"\n✅ PRODUCTO ENCONTRADO:")
            print(f"┌{'─' * 40}┐")
            print(f"│ 📋 ID: {producto.id_producto:<28} {estado} │")
            print(f"│ 📦 Nombre: {producto.nombre:<26} │")
            print(f"│ 📝 Descripción: {producto.descripcion:<22} │")
            print(f"│ 📁 Categoría: {producto.categoria.title():<22} │")
            print(f"│ 💰 Precio unidad: ${producto.precio_unidad:<17} │")
            print(f"│ 💰 Precio docena: ${producto.precio_docena:<16} │")
            print(f"│ 💰 Precio caja: ${producto.precio_caja:<18} │")
            print(f"│ 📊 Stock: {producto.stock:<26} │")
            print(f"└{'─' * 40}┘")
            return
        
        productos = self.producto_service.buscar_productos_por_nombre(criterio)
        productos_activos = [p for p in productos if p.activo]
        
        if productos_activos:
            print(f"\n🔍 Se encontraron {len(productos_activos)} productos activos:")
            for producto in productos_activos:
                stock_icon = "⚠️" if producto.tiene_stock_bajo() else "✅"
                print(f"   {stock_icon} {producto}")
        else:
            print("❌ No se encontraron productos activos.")
    
    def actualizar_producto(self):
        self._mostrar_titulo("✏️ ACTUALIZAR PRODUCTO")
        id_producto = input("👉 ID del producto a actualizar: ")
        
        producto = self.producto_service.obtener_producto(id_producto)
        if not producto:
            print("❌ Producto no encontrado.")
            return
        
        print(f"\n📦 Producto actual: {producto}")
        print("\n💡 Deja en blanco los campos que no quieras cambiar:")
        
        nuevos_datos = {}
        
        nombre = input(f"📦 Nuevo nombre [{producto.nombre}]: ")
        if nombre and validar_texto(nombre):
            nuevos_datos['nombre'] = nombre
        
        descripcion = input(f"📝 Nueva descripción [{producto.descripcion}]: ")
        if descripcion:
            nuevos_datos['descripcion'] = descripcion
        
        precio_unidad = input(f"💰 Nuevo precio unidad [${producto.precio_unidad}]: ")
        if precio_unidad and validar_precio(precio_unidad):
            nuevos_datos['precio_unidad'] = float(precio_unidad)
        
        precio_docena = input(f"💰 Nuevo precio docena [${producto.precio_docena}]: ")
        if precio_docena and validar_precio(precio_docena):
            nuevos_datos['precio_docena'] = float(precio_docena)
        
        precio_caja = input(f"💰 Nuevo precio caja [${producto.precio_caja}]: ")
        if precio_caja and validar_precio(precio_caja):
            nuevos_datos['precio_caja'] = float(precio_caja)
        
        stock = input(f"📊 Nuevo stock [{producto.stock}]: ")
        if stock and validar_entero_positivo(stock):
            nuevos_datos['stock'] = int(stock)
        
        if nuevos_datos:
            success, message = self.producto_service.actualizar_producto(id_producto, nuevos_datos)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ No se realizaron cambios.")
    
    def cambiar_estado_producto(self):
        self._mostrar_titulo("🔄 CAMBIAR ESTADO DE PRODUCTO")
        id_producto = input("👉 ID del producto: ")
        
        producto = self.producto_service.obtener_producto(id_producto)
        if not producto:
            print("❌ Producto no encontrado.")
            return
        
        estado_actual = "ACTIVO" if producto.activo else "INACTIVO"
        print(f"\n📦 Producto: {producto.nombre}")
        print(f"📊 Estado actual: {estado_actual}")
        
        print("\n🔄 OPCIONES:")
        print("1. ✅ Activar producto")
        print("2. ❌ Desactivar producto")
        print("3. ↩️ Cancelar")
        
        opcion = input("\n👉 Selecciona una opción (1-3): ")
        
        if opcion == "1":
            if producto.activo:
                print("❌ El producto ya está activo.")
            else:
                success, message = self.producto_service.actualizar_producto(id_producto, {'activo': True})
                print(f"\n{'✅' if success else '❌'} {message}")
        
        elif opcion == "2":
            if not producto.activo:
                print("❌ El producto ya está inactivo.")
            else:
                success, message = self.producto_service.actualizar_producto(id_producto, {'activo': False})
                print(f"\n{'✅' if success else '❌'} {message}")
        
        elif opcion == "3":
            print("✅ Operación cancelada.")
        
        else:
            print("❌ Opción inválida.")
    
    def ver_stock_bajo(self):
        self._mostrar_titulo("⚠️ PRODUCTOS CON STOCK BAJO")
        productos = self.producto_service.obtener_productos_stock_bajo()
        
        # Filtrar solo productos activos
        productos_activos = [p for p in productos if p.activo]
        
        if not productos_activos:
            print("✅ Todos los productos activos tienen stock suficiente.")
            return
        
        print(f"⚠️  Hay {len(productos_activos)} productos ACTIVOS con stock bajo:")
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'STOCK':<8} {'MÍNIMO':<8}")
        print("=" * 55)
        
        for producto in productos_activos:
            print(f"{producto.id_producto:<10} {producto.nombre:<25} {producto.stock:<8} {producto.stock_minimo:<8}")