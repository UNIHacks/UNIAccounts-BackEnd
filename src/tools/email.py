import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import config.base as CONFIG

# Configuración del servidor SMTP y las credenciales de autenticación
smtp_host = CONFIG.SMTP_HOST
smtp_port = CONFIG.SMTP_PORT
smtp_username = CONFIG.SMTP_USER
smtp_password = CONFIG.SMTP_PASSWORD

def generateHTML_forgot_code(code: str):
    with open("templates/forgot_password.html", "r") as file:
        html_content = file.read()
    html_content = html_content.replace("{{ codigo }}", code)
    return html_content
    

def sendEmail(destination: str, subject: str, html_content: str):
    
    # Crear el mensaje de correo electrónico
    message = MIMEMultipart()
    message['From'] = CONFIG.SMTP_USER
    message['To'] = destination
    message['Subject'] = subject

    # Cuerpo del correo electrónico
    html_body = MIMEText(html_content, 'html')
    message.attach(html_body)
    
    response = 'Error to Send Email'

    # Enviar el correo electrónico
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
        response = f'Success full send Email: {hideEmail(destination)}'
    
    return response
        
def hideEmail(email: str) -> str:
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    
    # Ocultar caracteres del nombre de usuario (solo muestra los primeros dos caracteres y los asteriscos)
    hidden_username = username[:2] + "*" * (len(username) - 2)
    
    # Ocultar caracteres del dominio (solo muestra el primer caracter y los asteriscos)
    hidden_domain = domain[0] + "*" * (len(domain) - 1)
    
    # Reconstruir el correo electrónico oculto
    hidden_email = hidden_username + "@" + hidden_domain
    
    return hidden_email
