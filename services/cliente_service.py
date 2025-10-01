import json
import os
from models.cliente import Cliente
from interfaces.cliente_interface import IClienteService

class ClienteService(IClienteService):
    def __init__(self, archivo_datos="data/clientes.json"):
        self.archivo_datos = archivo_datos
        self._crear_archivo_si_no_existe()
    
    def _crear_archivo_si_no_existe(self):
        os.makedirs(os.path.dirname(self.archivo_datos), exist_ok=True)
        if not os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'w') as f:
                json.dump([], f)
    
    def _cargar_clientes(self):
        try:
            with open(self.archivo_datos, 'r') as f:
                datos = json.load(f)
                return [Cliente.from_dict(cliente) for cliente in datos]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _guardar_clientes(self, clientes):
        with open(self.archivo_datos, 'w') as f:
            json.dump([cliente.to_dict() for cliente in clientes], f, indent=2)
    
    def registrar_cliente(self, cliente):
        clientes = self._cargar_clientes()
        if any(c.id_cliente == cliente.id_cliente for c in clientes):
            return False, "El ID del cliente ya existe"
        
        clientes.append(cliente)
        self._guardar_clientes(clientes)
        return True, "Cliente registrado exitosamente"
    
    def obtener_cliente(self, id_cliente):
        clientes = self._cargar_clientes()
        for cliente in clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def obtener_todos_clientes(self):
        return self._cargar_clientes()
    
    def buscar_clientes_por_nombre(self, nombre):
        clientes = self._cargar_clientes()
        return [c for c in clientes if nombre.lower() in c.nombre.lower()]
    
    def actualizar_cliente(self, id_cliente, datos_actualizados):
        clientes = self._cargar_clientes()
        for cliente in clientes:
            if cliente.id_cliente == id_cliente:
                for key, value in datos_actualizados.items():
                    if hasattr(cliente, key):
                        setattr(cliente, key, value)
                self._guardar_clientes(clientes)
                return True, "Cliente actualizado exitosamente"
        return False, "Cliente no encontrado"
    
    def eliminar_cliente(self, id_cliente):
        clientes = self._cargar_clientes()
        clientes_actualizados = [c for c in clientes if c.id_cliente != id_cliente]
        
        if len(clientes_actualizados) == len(clientes):
            return False, "Cliente no encontrado"
        
        self._guardar_clientes(clientes_actualizados)
        return True, "Cliente eliminado exitosamente"
    
    def filtrar_clientes_por_tipo(self, tipo_cliente):
        clientes = self._cargar_clientes()
        return [c for c in clientes if c.tipo_cliente.lower() == tipo_cliente.lower()]