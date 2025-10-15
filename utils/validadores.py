import re

def validar_email(email):
    """Valida que el email tenga un formato correcto"""
    if not email:
        return False
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    """Valida que el teléfono tenga solo números y sea de longitud razonable"""
    if not telefono:
        return False
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def validar_precio(precio):
    """Valida que el precio sea un número positivo"""
    try:
        precio_float = float(precio)
        return precio_float > 0
    except (ValueError, TypeError):
        return False

def validar_stock(stock):
    """Valida que el stock sea un número entero no negativo"""
    try:
        stock_int = int(stock)
        return stock_int >= 0
    except (ValueError, TypeError):
        return False

def validar_texto(texto):
    """Valida que el texto no esté vacío"""
    if not texto or not texto.strip():
        return False
    return True

def validar_numero_positivo(numero):
    """Valida que sea un número positivo"""
    try:
        num = float(numero)
        return num > 0
    except (ValueError, TypeError):
        return False

def validar_entero_positivo(numero):
    """Valida que sea un número entero positivo"""
    try:
        num = int(numero)
        return num >= 0
    except (ValueError, TypeError):
        return False

def validar_opcion_menu(opcion, max_opciones):
    """Valida que la opción del menú sea válida"""
    try:
        num = int(opcion)
        return 1 <= num <= max_opciones
    except (ValueError, TypeError):
        return False