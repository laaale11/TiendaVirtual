from abc import ABC, abstractmethod

class IPedidoService(ABC):
    @abstractmethod
    def registrar_pedido(self, pedido):
        pass
    
    @abstractmethod
    def obtener_pedido(self, id_pedido):
        pass
    
    @abstractmethod
    def obtener_todos_pedidos(self):
        pass
    
    @abstractmethod
    def actualizar_estado_pedido(self, id_pedido, nuevo_estado):
        pass
    
    @abstractmethod
    def cancelar_pedido(self, id_pedido):
        pass
    
    @abstractmethod
    def obtener_pedidos_por_cliente(self, id_cliente):
        pass
    
    @abstractmethod
    def obtener_pedidos_por_fecha(self, fecha):
        pass
    
    @abstractmethod
    def calcular_total_pedido(self, productos):
        pass