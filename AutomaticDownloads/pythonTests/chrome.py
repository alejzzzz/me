import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    # Configura la barra de progreso
    progress['maximum'] = 100
    for i in range(101):
        # Actualiza la barra de progreso
        progress['value'] = i
        # Actualiza la ventana para reflejar los cambios
        root.update_idletasks()
        time.sleep(0.05)  # Simula un proceso que toma tiempo
    # Muestra el mensaje de finalización
    label.config(text="Chrome se ha instalado correctamente.")
    start_button.config(text="Cerrar", command=root.destroy)

# Crea la ventana principal
root = tk.Tk()
root.title("Instalador de Chrome")

# Ajusta la ventana para que sea cuadrada y no redimensionable
window_size = 300  # Tamaño de la ventana (400x400 píxeles)
root.geometry(f"{window_size}x{window_size}")
root.resizable(False, False)

# Crea un frame principal para centrar el contenido verticalmente
main_frame = tk.Frame(root)
main_frame.pack(expand=True)  # Expande el frame para ocupar el espacio disponible

# Crea un label para mostrar el mensaje inicial
label = tk.Label(main_frame, text="Pulse para instalar Chrome")
label.pack(pady=10)

# Crea un frame para agregar márgenes a los lados de la barra de progreso
frame = tk.Frame(main_frame, padx=20)
frame.pack(pady=10)

# Crea una barra de progreso dentro del frame
progress = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

# Botón para iniciar la barra de progreso
start_button = tk.Button(main_frame, text="Instalar", command=start_progress)
start_button.pack(pady=10)

# Ejecuta la ventana
root.mainloop()
