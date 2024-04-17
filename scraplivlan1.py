from scrapli.driver.core import IOSXEDriver

# Definir los detalles de conexión al dispositivo
device = {
    "host": "192.168.1.1",          # Cambia esto por la dirección IP de tu dispositivo
    "auth_username": "tu_usuario",  # Cambia esto por tu nombre de usuario Telnet
    "auth_password": "tu_contraseña",# Cambia esto por tu contraseña Telnet
    "transport": "telnet",          # Especificar el protocolo de transporte (en este caso, Telnet)
    "port": 23                      # Puerto Telnet (por defecto es 23)
}

# Comandos de configuración para crear una VLAN
config_commands = [
    "configure terminal",
    "vlan 100",
    "name MiVLAN",
    "end"
]

# Establecer la conexión con el dispositivo
with IOSXEDriver(**device) as conn:
    # Enviar los comandos de configuración al dispositivo
    response = conn.send_configs(config_commands)

# Imprimir la salida del comando
print(response.result)
