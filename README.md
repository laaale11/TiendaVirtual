# ??? Tienda Virtual - Sistema de Gesti�n

Sistema completo de gesti�n para tiendas con interfaz de consola mejorada.

## ? Caracter�sticas Principales

- ?? **Gesti�n de Productos**: 3 precios (unidad, docena, caja), 5 categor�as, control de stock
- ?? **Gesti�n de Clientes**: Mayoristas/Minoristas, datos completos, filtrado por tipo
- ?? **Gesti�n de Pedidos**: Estados (Pendiente/Entregado/Cancelado), m�ltiples m�todos de pago
- ?? **Comunicaci�n**: Env�o simulado de WhatsApp y Email, historial de comunicaciones
- ?? **Persistencia**: Datos guardados en archivos JSON autom�ticamente
- ?? **Interfaz**: Consola con dise�o mejorado, tablas formateadas, validaciones

## ?? Instalaci�n y Ejecuci�n

\\\ash
# Clonar repositorio
git clone https://github.com/laaale11/TiendaVirtual.git
cd TiendaVirtual

# Ejecutar aplicaci�n
python main.py
\\\

## ??? Estructura del Proyecto

\\\
TiendaVirtual/
+-- models/          # Modelos de datos (Producto, Cliente, Pedido, Comunicaci�n)
+-- services/        # L�gica de negocio y persistencia
+-- managers/        # Controladores y men�s interactivos
+-- interfaces/      # Interfaces abstractas
+-- utils/           # Utilidades y helpers
+-- data/           # Archivos JSON de datos
+-- main.py         # Aplicaci�n principal
+-- README.md       # Documentaci�n
\\\

## ?? Uso R�pido

1. **Registrar Productos**: Gesti�n de Productos ? Registrar nuevo producto
2. **Registrar Clientes**: Gesti�n de Clientes ? Registrar nuevo cliente  
3. **Crear Pedidos**: Gesti�n de Pedidos ? Registrar nuevo pedido
4. **Comunicaci�n**: Comunicaci�n con Clientes ? Enviar mensaje/email

## ?? Datos Guardados

- \data/productos.json\ - Cat�logo completo
- \data/clientes.json\ - Base de clientes
- \data/pedidos.json\ - Historial de pedidos
- \data/comunicaciones.json\ - Registro de mensajes

## ??? Tecnolog�as

- **Python 3.7+**
- **Arquitectura en capas** (Models, Services, Managers, Interfaces)
- **Persistencia JSON** (Sin base de datos externa)
- **Interfaz de consola** con dise�o mejorado

## ????? Desarrollado por

[Alejandra P�rez](https://github.com/laaale11)

�Sistema desarrollado con ?? para gesti�n eficiente de tiendas!
