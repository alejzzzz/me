import os
import subprocess
import json
import time

nuevo_directorio = "C:\\Users\\Manuela\\Desktop\\CursoPro\\me\\prueba"  # Cambia esto a tu ruta deseada
os.chdir(nuevo_directorio)

# Cargar la configuración desde el archivo JSON
def cargar_configuracion(ruta_config):
    with open(ruta_config, 'r') as archivo:
        return json.load(archivo)

# Función para instalar un programa
def instalar_programa(nombre, detalles):
    ruta_instalador = detalles["path"]
    argumentos_silenciosos = detalles["silent_args"]
    
    # Convertir la ruta relativa a una ruta absoluta basada en el directorio del script
    ruta_instalador_absoluta = os.path.abspath(ruta_instalador)
    
    if os.path.exists(ruta_instalador_absoluta):
        print(f"Instalando {nombre}...")
        # Ejecutar el instalador
        proceso = subprocess.Popen([ruta_instalador_absoluta] + argumentos_silenciosos.split(), shell=True)
        proceso.wait()  # Esperar a que el proceso termine
        if proceso.returncode == 0:
            print(f"{nombre} instalado correctamente.")
        else:
            print(f"Error al instalar {nombre}. Código de retorno: {proceso.returncode}")
    else:
        print(f"El instalador de {nombre} no se encuentra en la ruta especificada: {ruta_instalador_absoluta}")

# Ruta al archivo de configuración
ruta_config = "config.json"

# Cargar la configuración
configuracion = cargar_configuracion(ruta_config)

# Instalar todos los programas uno a uno
for nombre, detalles in configuracion["programas"].items():
    instalar_programa(nombre, detalles)
    time.sleep(2)  # Pausa de 2 segundos entre instalaciones, opcional

 
