import re

def validar_email(email):
    """Valida que el email tenga un formato correcto"""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    """Valida que el teléfono tenga solo números y sea de longitud razonable"""
    return telefono.isdigit() and 7 <= len(telefono) <= 15

def validar_precio(precio):
    """Valida que el precio sea un número positivo"""
    try:
        precio_float = float(precio)
        return precio_float > 0
    except ValueError:
        return False

def validar_stock(stock):
    """Valida que el stock sea un número entero no negativo"""
    try:
        stock_int = int(stock)
        return stock_int >= 0
    except ValueError:
        return False