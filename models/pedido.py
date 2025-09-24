from datetime import datetime

class Pedido:
    def __init__(self, id, cliente_id, productos=None, total=0.0):
        """
        Constructor de la clase Pedido
        
        Args:
            id (int): Identificador único del pedido
            cliente_id (int): ID del cliente que realiza el pedido
            productos (list, optional): Lista de productos. Defaults to [].
            total (float, optional): Total del pedido. Defaults to 0.0.
        """
        self.id = id
        self.cliente_id = cliente_id
        self.productos = productos if productos else []
        self.total = total
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.estado = "pendiente"  # Estados: pendiente, confirmado, enviado, entregado, cancelado

    def __str__(self):
        """Representación en string del pedido"""
        return f"Pedido #{self.id} - Cliente: {self.cliente_id} - Total: ${self.total:.2f} - Estado: {self.estado}"

    def obtener_info_detallada(self):
        """Obtiene información detallada del pedido"""
        info = f"""
        === INFORMACIÓN DEL PEDIDO ===
        ID: {self.id}
        Cliente ID: {self.cliente_id}
        Fecha: {self.fecha}
        Estado: {self.estado.upper()}
        Total: ${self.total:.2f}
        Productos ({len(self.productos)}):
        """
        
        for i, producto in enumerate(self.productos, 1):
            info += f"          {i}. {producto}\n"
            
        return info

    def agregar_producto(self, producto, precio):
        """Agrega un producto al pedido"""
        self.productos.append(f"{producto} - ${precio:.2f}")
        self.total += precio
        return f"Producto '{producto}' agregado. Nuevo total: ${self.total:.2f}"

    def eliminar_producto(self, indice):
        """Elimina un producto del pedido por índice"""
        if 0 <= indice < len(self.productos):
            producto_eliminado = self.productos.pop(indice)
            # Extraer el precio del producto eliminado (asumiendo formato "Producto - $precio")
            try:
                precio = float(producto_eliminado.split('$')[-1])
                self.total -= precio
            except:
                pass  # Si no se puede extraer el precio, no hacemos nada
            return f"Producto eliminado. Nuevo total: ${self.total:.2f}"
        else:
            return "Índice inválido"

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del pedido"""
        estados_validos = ["pendiente", "confirmado", "enviado", "entregado", "cancelado"]
        
        if nuevo_estado.lower() in estados_validos:
            estado_anterior = self.estado
            self.estado = nuevo_estado.lower()
            return f"Estado cambiado de '{estado_anterior}' a '{self.estado}'"
        else:
            estados_str = ", ".join(estados_validos)
            raise ValueError(f"Estado inválido. Estados válidos: {estados_str}")

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al total del pedido"""
        if 0 < porcentaje <= 100:
            descuento = self.total * (porcentaje / 100)
            self.total -= descuento
            return f"Descuento del {porcentaje}% aplicado. Descuento: ${descuento:.2f} - Nuevo total: ${self.total:.2f}"
        else:
            raise ValueError("El porcentaje debe estar entre 1 y 100")

    def esta_activo(self):
        """Verifica si el pedido está activo (no cancelado ni entregado)"""
        return self.estado not in ["entregado", "cancelado"]
    