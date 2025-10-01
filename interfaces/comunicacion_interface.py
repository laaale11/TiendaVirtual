from abc import ABC, abstractmethod

class IComunicacionService(ABC):
    @abstractmethod
    def enviar_whatsapp(self, telefono, mensaje):
        pass
    
    @abstractmethod
    def enviar_email(self, email, asunto, mensaje):
        pass
    
    @abstractmethod
    def registrar_comunicacion(self, comunicacion):
        pass
    
    @abstractmethod
    def obtener_historial_comunicaciones(self, id_cliente=None):
        pass