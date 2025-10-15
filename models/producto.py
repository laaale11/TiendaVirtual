class Producto:
    CATEGORIAS_PERMITIDAS = [
        "maquillaje", 
        "material escolar", 
        "herramientas de trabajo", 
        "cocina", 
        "plásticos"
    ]
    
    def __init__(self, id_producto, nombre, descripcion, precio_unidad, precio_docena, precio_caja, stock, categoria, stock_minimo=10, activo=True):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_unidad = precio_unidad
        self.precio_docena = precio_docena
        self.precio_caja = precio_caja
        self.stock = stock
        self.categoria = self._validar_categoria(categoria)
        self.stock_minimo = stock_minimo
        self.activo = activo  # Nuevo: estado activo/inactivo
    
    def _validar_categoria(self, categoria):
        if categoria.lower() not in [cat.lower() for cat in self.CATEGORIAS_PERMITIDAS]:
            raise ValueError(f"Categoría '{categoria}' no permitida")
        return categoria.lower()
    
    def actualizar_stock(self, cantidad):
        self.stock += cantidad
    
    def tiene_stock_bajo(self):
        return self.stock <= self.stock_minimo
    
    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio_unidad': self.precio_unidad,
            'precio_docena': self.precio_docena,
            'precio_caja': self.precio_caja,
            'stock': self.stock,
            'categoria': self.categoria,
            'stock_minimo': self.stock_minimo,
            'activo': self.activo  # Nuevo campo
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id_producto'],
            data['nombre'],
            data['descripcion'],
            data['precio_unidad'],
            data['precio_docena'],
            data['precio_caja'],
            data['stock'],
            data['categoria'],
            data.get('stock_minimo', 10),
            data.get('activo', True)  # Nuevo campo
        )
    
    def __str__(self):
        estado = "✅" if self.activo else "❌"
        return f"{estado} {self.id_producto}: {self.nombre} - Uni:${self.precio_unidad} (Stock: {self.stock})"