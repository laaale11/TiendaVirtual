from abc import ABC, abstractmethod

class IProductoService(ABC):
    @abstractmethod
    def registrar_producto(self, producto):
        pass
    
    @abstractmethod
    def obtener_producto(self, id_producto):
        pass
    
    @abstractmethod
    def obtener_todos_productos(self):
        pass
    
    @abstractmethod
    def buscar_productos_por_nombre(self, nombre):
        pass
    
    @abstractmethod
    def actualizar_producto(self, id_producto, datos_actualizados):
        pass
    
    @abstractmethod
    def eliminar_producto(self, id_producto):
        pass
    
    @abstractmethod
    def obtener_productos_stock_bajo(self):
        pass
    
    @abstractmethod
    def actualizar_stock(self, id_producto, cantidad):
        pass