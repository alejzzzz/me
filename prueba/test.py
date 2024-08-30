import os
import subprocess
import json

# Cargar la configuración desde el archivo JSON
def cargar_configuracion(ruta_config):
    with open(ruta_config, 'r') as archivo:
        return json.load(archivo)

# Función para instalar un programa
def instalar_programa(nombre, detalles):
    ruta_instalador = detalles["path"]
    argumentos_silenciosos = detalles["silent_args"]
    
    if os.path.exists(ruta_instalador):
        print(f"Instalando {nombre}...")
        subprocess.run([ruta_instalador] + argumentos_silenciosos.split(), check=True)
        print(f"{nombre} instalado correctamente.")
    else:
        print(f"El instalador de {nombre} no se encuentra en la ruta especificada: {ruta_instalador}")

# Ruta al archivo de configuración
ruta_config = "C:\\Users\\user\\Desktop\\CursoPro\\prueba\\config.json"

# Cargar la configuración
configuracion = cargar_configuracion(ruta_config)

# Instalar todos los programas
for nombre, detalles in configuracion["programas"].items():
    instalar_programa(nombre, detalles)
