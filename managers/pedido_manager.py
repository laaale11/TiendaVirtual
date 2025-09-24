from models.pedido import Pedido
from data.clientes_ejemplo import pedidos_ejemplo
from managers.cliente_manager import manager_clientes

class PedidoManager:
    def __init__(self, datos_iniciales=None):
        """
        Manager para gestionar pedidos
        
        Args:
            datos_iniciales (list): Lista inicial de pedidos (opcional)
        """
        self.pedidos = datos_iniciales if datos_iniciales else []
        self.ultimo_id = max([p.id for p in self.pedidos]) if self.pedidos else 0

    def crear_pedido(self, cliente_id, productos=None):
        """Crea un nuevo pedido para un cliente"""
        # Verificar que el cliente existe y está activo
        cliente = manager_clientes.buscar_por_id(cliente_id)
        if not cliente:
            raise ValueError(f"No se encontró cliente con ID: {cliente_id}")
        if not cliente.activo:
            raise ValueError(f"El cliente {cliente.nombre} está inactivo")
        
        self.ultimo_id += 1
        nuevo_pedido = Pedido(self.ultimo_id, cliente_id, productos)
        self.pedidos.append(nuevo_pedido)
        
        # Asignar el pedido al cliente
        cliente.agregar_pedido(self.ultimo_id)
        
        return nuevo_pedido

    def buscar_por_id(self, id):
        """Busca un pedido por ID"""
        for pedido in self.pedidos:
            if pedido.id == id:
                return pedido
        return None

    def buscar_por_cliente(self, cliente_id):
        """Busca todos los pedidos de un cliente"""
        return [pedido for pedido in self.pedidos if pedido.cliente_id == cliente_id]

    def listar_pedidos(self, estado=None, cliente_id=None):
        """Lista pedidos con filtros opcionales"""
        resultados = self.pedidos
        
        if estado:
            resultados = [p for p in resultados if p.estado == estado]
        if cliente_id:
            resultados = [p for p in resultados if p.cliente_id == cliente_id]
            
        return resultados

    def cambiar_estado_pedido(self, pedido_id, nuevo_estado):
        """Cambia el estado de un pedido"""
        pedido = self.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError(f"No se encontró pedido con ID: {pedido_id}")
        
        return pedido.cambiar_estado(nuevo_estado)

    def agregar_producto_pedido(self, pedido_id, producto, precio):
        """Agrega un producto a un pedido existente"""
        pedido = self.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError(f"No se encontró pedido con ID: {pedido_id}")
        
        if not pedido.esta_activo():
            raise ValueError("No se pueden agregar productos a un pedido cancelado o entregado")
        
        return pedido.agregar_producto(producto, precio)

    def eliminar_producto_pedido(self, pedido_id, indice_producto):
        """Elimina un producto de un pedido"""
        pedido = self.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError(f"No se encontró pedido con ID: {pedido_id}")
        
        if not pedido.esta_activo():
            raise ValueError("No se pueden eliminar productos de un pedido cancelado o entregado")
        
        return pedido.eliminar_producto(indice_producto)

    def aplicar_descuento_pedido(self, pedido_id, porcentaje):
        """Aplica un descuento a un pedido"""
        pedido = self.buscar_por_id(pedido_id)
        if not pedido:
            raise ValueError(f"No se encontró pedido con ID: {pedido_id}")
        
        return pedido.aplicar_descuento(porcentaje)

    def obtener_estadisticas(self):
        """Obtiene estadísticas de los pedidos"""
        total_pedidos = len(self.pedidos)
        total_ventas = sum(pedido.total for pedido in self.pedidos)
        
        # Pedidos por estado
        estados = {}
        for pedido in self.pedidos:
            estados[pedido.estado] = estados.get(pedido.estado, 0) + 1
        
        # Pedido con mayor valor
        pedido_mayor_valor = max(self.pedidos, key=lambda p: p.total) if self.pedidos else None
        
        # Cliente con más pedidos
        from collections import Counter
        cliente_pedidos = Counter(pedido.cliente_id for pedido in self.pedidos)
        cliente_mas_pedidos = cliente_pedidos.most_common(1)[0] if cliente_pedidos else (None, 0)
        
        return {
            "total_pedidos": total_pedidos,
            "total_ventas": total_ventas,
            "venta_promedio": total_ventas / total_pedidos if total_pedidos else 0,
            "pedidos_por_estado": estados,
            "pedido_mayor_valor": pedido_mayor_valor.id if pedido_mayor_valor else None,
            "valor_mayor_pedido": pedido_mayor_valor.total if pedido_mayor_valor else 0,
            "cliente_mas_pedidos": cliente_mas_pedidos[0],
            "total_pedidos_cliente": cliente_mas_pedidos[1]
        }

    def cancelar_pedido(self, pedido_id):
        """Cancela un pedido"""
        return self.cambiar_estado_pedido(pedido_id, "cancelado")

    def obtener_pedidos_activos(self):
        """Obtiene todos los pedidos activos (no entregados ni cancelados)"""
        return [pedido for pedido in self.pedidos if pedido.esta_activo()]

    def exportar_reporte(self, formato="simple"):
        """Exporta un reporte de pedidos"""
        if formato == "simple":
            reporte = "=== REPORTE DE PEDIDOS ===\n\n"
            for pedido in self.pedidos:
                reporte += f"Pedido #{pedido.id} - Cliente: {pedido.cliente_id}\n"
                reporte += f"Estado: {pedido.estado} - Total: ${pedido.total:.2f}\n"
                reporte += f"Productos: {len(pedido.productos)} - Fecha: {pedido.fecha}\n"
                reporte += "-" * 50 + "\n"
        
        return reporte

# Crear instancia global con datos de ejemplo
manager_pedidos = PedidoManager(pedidos_ejemplo)

if __name__ == "__main__":
    print("=== PRUEBA DEL PEDIDO MANAGER ===")
    print(f"Pedidos cargados: {len(manager_pedidos.pedidos)}")
    
    # Probar funcionalidades básicas
    print("\n1. Listar pedidos activos:")
    activos = manager_pedidos.obtener_pedidos_activos()
    print(f"Pedidos activos: {len(activos)}")
    
    print("\n2. Estadísticas:")
    stats = manager_pedidos.obtener_estadisticas()
    for key, value in stats.items():
        if key != "pedidos_por_estado":
            print(f"   {key}: {value}")
    
    print("   pedidos_por_estado:")
    for estado, cantidad in stats["pedidos_por_estado"].items():
        print(f"     {estado}: {cantidad}")