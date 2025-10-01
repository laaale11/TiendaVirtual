try:
    from .producto_service import ProductoService
    from .cliente_service import ClienteService
    from .pedido_service import PedidoService
    from .comunicacion_service import ComunicacionService
except ImportError:
    from producto_service import ProductoService
    from cliente_service import ClienteService
    from pedido_service import PedidoService
    from comunicacion_service import ComunicacionService

__all__ = ['ProductoService', 'ClienteService', 'PedidoService', 'ComunicacionService']