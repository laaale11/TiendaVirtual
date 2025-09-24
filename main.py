from interfaces.consola import InterfazConsola

def main():
    """Función principal de la aplicación"""
    try:
        app = InterfazConsola()
        app.iniciar()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta pronto!")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()