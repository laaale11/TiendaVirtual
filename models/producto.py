class Producto:
    # Lista de categorías permitidas
    CATEGORIAS_PERMITIDAS = [
        "maquillaje", 
        "material escolar", 
        "herramientas de trabajo", 
        "cocina", 
        "plásticos"
    ]
    
    def __init__(self, id_producto, nombre, descripcion, precio_unidad, precio_docena, precio_caja, stock, categoria, stock_minimo=10):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_unidad = precio_unidad
        self.precio_docena = precio_docena
        self.precio_caja = precio_caja
        self.stock = stock
        self.categoria = self._validar_categoria(categoria)
        self.stock_minimo = stock_minimo
    
    def _validar_categoria(self, categoria):
        """Valida que la categoría esté en la lista permitida"""
        if categoria.lower() not in [cat.lower() for cat in self.CATEGORIAS_PERMITIDAS]:
            raise ValueError(f"Categoría '{categoria}' no permitida. Use: {', '.join(self.CATEGORIAS_PERMITIDAS)}")
        return categoria.lower()
    
    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto"""
        self.stock += cantidad
    
    def tiene_stock_bajo(self):
        """Verifica si el stock está por debajo del mínimo"""
        return self.stock <= self.stock_minimo
    
    def to_dict(self):
        """Convierte el producto a diccionario para almacenamiento"""
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio_unidad': self.precio_unidad,
            'precio_docena': self.precio_docena,
            'precio_caja': self.precio_caja,
            'stock': self.stock,
            'categoria': self.categoria,
            'stock_minimo': self.stock_minimo
        }
    
    @classmethod
    def from_dict(cls, data):
        """Crea un producto desde un diccionario"""
        return cls(
            data['id_producto'],
            data['nombre'],
            data['descripcion'],
            data['precio_unidad'],
            data['precio_docena'],
            data['precio_caja'],
            data['stock'],
            data['categoria'],
            data.get('stock_minimo', 10)
        )
    
    def __str__(self):
        return f"{self.id_producto}: {self.nombre} - Uni:${self.precio_unidad} Doc:${self.precio_docena} Caja:${self.precio_caja} (Stock: {self.stock})"