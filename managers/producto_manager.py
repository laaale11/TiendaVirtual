from services.producto_service import ProductoService
from models.producto import Producto

class ProductoManager:
    def __init__(self):
        self.producto_service = ProductoService()
    
    def registrar_producto(self):
        print("\n=== REGISTRAR NUEVO PRODUCTO ===")
        
        try:
            id_producto = input("ID producto: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            
            print("\n💲 PRECIOS:")
            precio_unidad = float(input("Precio por unidad: $"))
            precio_docena = float(input("Precio por docena: $"))
            precio_caja = float(input("Precio por caja: $"))
            
            stock = int(input("Stock disponible: "))
            
            # Mostrar categorías disponibles
            print("\n📁 CATEGORÍAS:")
            for i, categoria in enumerate(Producto.CATEGORIAS_PERMITIDAS, 1):
                print(f"  {i}. {categoria.title()}")
            
            categoria_num = input(f"\nSelecciona categoría (1-{len(Producto.CATEGORIAS_PERMITIDAS)}): ")
            try:
                categoria_index = int(categoria_num) - 1
                categoria = Producto.CATEGORIAS_PERMITIDAS[categoria_index]
            except (ValueError, IndexError):
                print("❌ Selección inválida. Usando categoría por defecto.")
                categoria = Producto.CATEGORIAS_PERMITIDAS[0]
            
            stock_minimo = int(input("Stock mínimo (default 10): ") or "10")
            
            producto = Producto(id_producto, nombre, descripcion, precio_unidad, precio_docena, precio_caja, stock, categoria, stock_minimo)
            success, message = self.producto_service.registrar_producto(producto)
            
            print(f"\n{'✅' if success else '❌'} {message}")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    def ver_catalogo(self):
        print("\n=== CATÁLOGO DE PRODUCTOS ===")
        productos = self.producto_service.obtener_todos_productos()
        
        if not productos:
            print("No hay productos registrados.")
            return
        
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'CATEGORÍA':<20} {'PRECIO UNI':<12} {'PRECIO DOC':<12} {'PRECIO CAJA':<12} {'STOCK':<8}")
        print("=" * 100)
        
        for producto in productos:
            stock_icon = "⚠️" if producto.tiene_stock_bajo() else "✅"
            print(f"{producto.id_producto:<10} {producto.nombre:<25} {producto.categoria.title():<20} ${producto.precio_unidad:<11} ${producto.precio_docena:<11} ${producto.precio_caja:<11} {stock_icon} {producto.stock:<6}")
    
    def buscar_producto(self):
        print("\n=== BUSCAR PRODUCTO ===")
        criterio = input("Buscar por ID o nombre: ")
        
        # Intentar buscar por ID primero
        producto = self.producto_service.obtener_producto(criterio)
        if producto:
            print(f"\n✅ PRODUCTO ENCONTRADO:")
            print(f"   ID: {producto.id_producto}")
            print(f"   Nombre: {producto.nombre}")
            print(f"   Descripción: {producto.descripcion}")
            print(f"   Categoría: {producto.categoria.title()}")
            print(f"   Precio por unidad: ${producto.precio_unidad}")
            print(f"   Precio por docena: ${producto.precio_docena}")
            print(f"   Precio por caja: ${producto.precio_caja}")
            print(f"   Stock disponible: {producto.stock}")
            print(f"   Stock mínimo: {producto.stock_minimo}")
            return
        
        # Si no encuentra por ID, buscar por nombre
        productos = self.producto_service.buscar_productos_por_nombre(criterio)
        if productos:
            print(f"\n🔍 Se encontraron {len(productos)} productos:")
            for producto in productos:
                stock_icon = "⚠️" if producto.tiene_stock_bajo() else "✅"
                print(f"   {stock_icon} {producto}")
        else:
            print("❌ No se encontraron productos.")
    
    def actualizar_producto(self):
        print("\n=== ACTUALIZAR PRODUCTO ===")
        id_producto = input("ID del producto a actualizar: ")
        
        producto = self.producto_service.obtener_producto(id_producto)
        if not producto:
            print("❌ Producto no encontrado.")
            return
        
        print(f"\nProducto actual: {producto}")
        print("\nDeja en blanco los campos que no quieras cambiar:")
        
        nuevos_datos = {}
        nombre = input(f"Nuevo nombre [{producto.nombre}]: ")
        if nombre: nuevos_datos['nombre'] = nombre
        
        descripcion = input(f"Nueva descripción [{producto.descripcion}]: ")
        if descripcion: nuevos_datos['descripcion'] = descripcion
        
        precio_unidad = input(f"Nuevo precio unidad [${producto.precio_unidad}]: ")
        if precio_unidad: nuevos_datos['precio_unidad'] = float(precio_unidad)
        
        precio_docena = input(f"Nuevo precio docena [${producto.precio_docena}]: ")
        if precio_docena: nuevos_datos['precio_docena'] = float(precio_docena)
        
        precio_caja = input(f"Nuevo precio caja [${producto.precio_caja}]: ")
        if precio_caja: nuevos_datos['precio_caja'] = float(precio_caja)
        
        stock = input(f"Nuevo stock [{producto.stock}]: ")
        if stock: nuevos_datos['stock'] = int(stock)
        
        # Actualizar categoría con menú
        print(f"\nCategoría actual: {producto.categoria.title()}")
        print("Categorías disponibles:")
        for i, categoria in enumerate(Producto.CATEGORIAS_PERMITIDAS, 1):
            print(f"  {i}. {categoria.title()}")
        
        categoria_num = input(f"\nNueva categoría (1-{len(Producto.CATEGORIAS_PERMITIDAS)}, Enter para mantener): ")
        if categoria_num:
            try:
                categoria_index = int(categoria_num) - 1
                nuevos_datos['categoria'] = Producto.CATEGORIAS_PERMITIDAS[categoria_index]
            except (ValueError, IndexError):
                print("❌ Selección inválida. Manteniendo categoría actual.")
        
        stock_minimo = input(f"Nuevo stock mínimo [{producto.stock_minimo}]: ")
        if stock_minimo: nuevos_datos['stock_minimo'] = int(stock_minimo)
        
        if nuevos_datos:
            success, message = self.producto_service.actualizar_producto(id_producto, nuevos_datos)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ No se realizaron cambios.")
    
    def eliminar_producto(self):
        print("\n=== ELIMINAR PRODUCTO ===")
        id_producto = input("ID del producto a eliminar: ")
        
        producto = self.producto_service.obtener_producto(id_producto)
        if not producto:
            print("❌ Producto no encontrado.")
            return
        
        confirmacion = input(f"¿Estás seguro de eliminar {producto.nombre}? (s/n): ")
        if confirmacion.lower() == 's':
            success, message = self.producto_service.eliminar_producto(id_producto)
            print(f"\n{'✅' if success else '❌'} {message}")
        else:
            print("❌ Eliminación cancelada.")
    
    def ver_stock_bajo(self):
        print("\n=== PRODUCTOS CON STOCK BAJO ===")
        productos = self.producto_service.obtener_productos_stock_bajo()
        
        if not productos:
            print("✅ Todos los productos tienen stock suficiente.")
            return
        
        print(f"⚠️  Hay {len(productos)} productos con stock bajo:")
        print(f"\n{'ID':<10} {'NOMBRE':<25} {'CATEGORÍA':<20} {'STOCK':<8} {'MÍNIMO':<8}")
        print("=" * 75)
        
        for producto in productos:
            print(f"{producto.id_producto:<10} {producto.nombre:<25} {producto.categoria.title():<20} {producto.stock:<8} {producto.stock_minimo:<8}")