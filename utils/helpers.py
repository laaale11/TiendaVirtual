from datetime import datetime

def formatear_fecha(fecha):
    """Formatea una fecha a string legible"""
    if isinstance(fecha, str):
        return fecha
    return fecha.strftime("%d/%m/%Y %H:%M")

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input("\nPresiona Enter para continuar...")

def mostrar_titulo(titulo):
    """Muestra un título formateado"""
    print(f"\n{'='*50}")
    print(f" {titulo}")
    print(f"{'='*50}")