import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models.comunicacion import Comunicacion
from interfaces.comunicacion_interface import IComunicacionService

class ComunicacionService(IComunicacionService):
    def __init__(self, archivo_datos="data/comunicaciones.json"):
        self.archivo_datos = archivo_datos
        self._crear_archivo_si_no_existe()
    
    def _crear_archivo_si_no_existe(self):
        os.makedirs(os.path.dirname(self.archivo_datos), exist_ok=True)
        if not os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'w') as f:
                json.dump([], f)
    
    def _cargar_comunicaciones(self):
        try:
            with open(self.archivo_datos, 'r') as f:
                datos = json.load(f)
                return [Comunicacion.from_dict(com) for com in datos]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _guardar_comunicaciones(self, comunicaciones):
        with open(self.archivo_datos, 'w') as f:
            json.dump([com.to_dict() for com in comunicaciones], f, indent=2)
    
    def enviar_whatsapp(self, telefono, mensaje):
        # Simulación de envío de WhatsApp
        print(f"📱 Enviando WhatsApp al {telefono}: {mensaje}")
        return True, "Mensaje de WhatsApp enviado (simulación)"
    
    def enviar_email(self, email, asunto, mensaje):
        try:
            # Simulación de envío de email
            print(f"📧 Enviando email a {email}: {asunto} - {mensaje}")
            return True, "Email enviado (simulación)"
        except Exception as e:
            return False, f"Error al enviar email: {str(e)}"
    
    def registrar_comunicacion(self, comunicacion):
        comunicaciones = self._cargar_comunicaciones()
        comunicaciones.append(comunicacion)
        self._guardar_comunicaciones(comunicaciones)
        return True, "Comunicación registrada"
    
    def obtener_historial_comunicaciones(self, id_cliente=None):
        comunicaciones = self._cargar_comunicaciones()
        if id_cliente:
            return [c for c in comunicaciones if c.id_cliente == id_cliente]
        return comunicaciones