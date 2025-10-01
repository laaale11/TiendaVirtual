# ??? Tienda Virtual - Sistema de Gestión

Sistema completo de gestión para tiendas con interfaz de consola mejorada.

## ? Características Principales

- ?? **Gestión de Productos**: 3 precios (unidad, docena, caja), 5 categorías, control de stock
- ?? **Gestión de Clientes**: Mayoristas/Minoristas, datos completos, filtrado por tipo
- ?? **Gestión de Pedidos**: Estados (Pendiente/Entregado/Cancelado), múltiples métodos de pago
- ?? **Comunicación**: Envío simulado de WhatsApp y Email, historial de comunicaciones
- ?? **Persistencia**: Datos guardados en archivos JSON automáticamente
- ?? **Interfaz**: Consola con diseño mejorado, tablas formateadas, validaciones

## ?? Instalación y Ejecución

\\\ash
# Clonar repositorio
git clone https://github.com/laaale11/TiendaVirtual.git
cd TiendaVirtual

# Ejecutar aplicación
python main.py
\\\

## ??? Estructura del Proyecto

\\\
TiendaVirtual/
+-- models/          # Modelos de datos (Producto, Cliente, Pedido, Comunicación)
+-- services/        # Lógica de negocio y persistencia
+-- managers/        # Controladores y menús interactivos
+-- interfaces/      # Interfaces abstractas
+-- utils/           # Utilidades y helpers
+-- data/           # Archivos JSON de datos
+-- main.py         # Aplicación principal
+-- README.md       # Documentación
\\\

## ?? Uso Rápido

1. **Registrar Productos**: Gestión de Productos ? Registrar nuevo producto
2. **Registrar Clientes**: Gestión de Clientes ? Registrar nuevo cliente  
3. **Crear Pedidos**: Gestión de Pedidos ? Registrar nuevo pedido
4. **Comunicación**: Comunicación con Clientes ? Enviar mensaje/email

## ?? Datos Guardados

- \data/productos.json\ - Catálogo completo
- \data/clientes.json\ - Base de clientes
- \data/pedidos.json\ - Historial de pedidos
- \data/comunicaciones.json\ - Registro de mensajes

## ??? Tecnologías

- **Python 3.7+**
- **Arquitectura en capas** (Models, Services, Managers, Interfaces)
- **Persistencia JSON** (Sin base de datos externa)
- **Interfaz de consola** con diseño mejorado

## ????? Desarrollado por

[Alejandra Pérez](https://github.com/laaale11)

¡Sistema desarrollado con ?? para gestión eficiente de tiendas!
