from services.comunicacion_service import ComunicacionService
from services.cliente_service import ClienteService
from models.comunicacion import Comunicacion
import random

class ComunicacionManager:
    def __init__(self):
        self.comunicacion_service = ComunicacionService()
        self.cliente_service = ClienteService()
    
    def enviar_whatsapp(self):
        print("\n=== ENVIAR MENSAJE POR WHATSAPP ===")
        
        id_cliente = input("ID del cliente: ")
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        print(f"\n📱 CLIENTE: {cliente.nombre}")
        print(f"📞 CELULAR: {cliente.celular}")
        
        mensaje = input("\nMensaje: ")
        
        # Simular envío de WhatsApp
        print(f"\n📤 Enviando WhatsApp al {cliente.celular}...")
        print(f"💬 Mensaje: {mensaje}")
        
        success = True
        message = f"Mensaje de WhatsApp enviado a {cliente.nombre}"
        
        if success:
            # Registrar la comunicación
            id_comunicacion = f"WA_{random.randint(1000, 9999)}"
            comunicacion = Comunicacion(id_comunicacion, id_cliente, "WhatsApp", mensaje, cliente.celular)
            self.comunicacion_service.registrar_comunicacion(comunicacion)
        
        print(f"\n{'✅' if success else '❌'} {message}")
    
    def enviar_email(self):
        print("\n=== ENVIAR CORREO ELECTRÓNICO ===")
        
        id_cliente = input("ID del cliente: ")
        cliente = self.cliente_service.obtener_cliente(id_cliente)
        if not cliente:
            print("❌ Cliente no encontrado.")
            return
        
        print(f"\n📧 CLIENTE: {cliente.nombre}")
        print(f"📨 EMAIL: {cliente.email}")
        
        asunto = input("Asunto: ")
        mensaje = input("Mensaje: ")
        
        # Simular envío de email
        print(f"\n📤 Enviando email a {cliente.email}...")
        print(f"📋 Asunto: {asunto}")
        print(f"💬 Mensaje: {mensaje}")
        
        success = True
        message = f"Email enviado a {cliente.nombre}"
        
        if success:
            # Registrar la comunicación
            id_comunicacion = f"EM_{random.randint(1000, 9999)}"
            comunicacion = Comunicacion(id_comunicacion, id_cliente, "Email", mensaje, cliente.email)
            self.comunicacion_service.registrar_comunicacion(comunicacion)
        
        print(f"\n{'✅' if success else '❌'} {message}")
    
    def ver_historial(self):
        print("\n=== HISTORIAL DE COMUNICACIONES ===")
        
        id_cliente = input("ID del cliente (deja vacío para ver todos): ")
        
        if id_cliente:
            cliente = self.cliente_service.obtener_cliente(id_cliente)
            if not cliente:
                print("❌ Cliente no encontrado.")
                return
            comunicaciones = self.comunicacion_service.obtener_historial_comunicaciones(id_cliente)
            print(f"\n📞 COMUNICACIONES CON {cliente.nombre.upper()}:")
        else:
            comunicaciones = self.comunicacion_service.obtener_historial_comunicaciones()
            print(f"\n📞 TODAS LAS COMUNICACIONES:")
        
        if not comunicaciones:
            print("   No hay comunicaciones registradas.")
            return
        
        print(f"\n{'FECHA':<20} {'CLIENTE':<20} {'MEDIO':<12} {'MENSAJE':<30}")
        print("=" * 85)
        
        for com in comunicaciones:
            cliente = self.cliente_service.obtener_cliente(com.id_cliente)
            nombre_cliente = cliente.nombre if cliente else "Cliente no encontrado"
            tipo_icon = "📱" if com.tipo == "WhatsApp" else "📧"
            mensaje_corto = com.mensaje[:27] + "..." if len(com.mensaje) > 30 else com.mensaje
            
            print(f"{com.fecha.strftime('%d/%m/%Y %H:%M'):<20} {nombre_cliente:<20} {tipo_icon} {com.tipo:<10} {mensaje_corto:<30}")