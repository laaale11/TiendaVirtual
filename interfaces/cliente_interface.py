from abc import ABC, abstractmethod

class IClienteService(ABC):
    @abstractmethod
    def registrar_cliente(self, cliente):
        pass
    
    @abstractmethod
    def obtener_cliente(self, id_cliente):
        pass
    
    @abstractmethod
    def obtener_todos_clientes(self):
        pass
    
    @abstractmethod
    def buscar_clientes_por_nombre(self, nombre):
        pass
    
    @abstractmethod
    def actualizar_cliente(self, id_cliente, datos_actualizados):
        pass
    
    @abstractmethod
    def eliminar_cliente(self, id_cliente):
        pass
    
    @abstractmethod
    def filtrar_clientes_por_tipo(self, tipo_cliente):
        pass