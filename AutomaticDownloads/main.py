import os
import subprocess
from pywinauto.application import Application

#abrir la aplicación
subprocess.Popen([r'installers/winrar.exe'])

# conectar la aplicación con pywinauto
app = Application().connect(path=r"installers/winrar.exe")

#establecer (WinRAR 6.11) como la ventana 1
ventana1 = app.window(title="WinRAR 6.11")
ventana1.set_focus()

#presionar enter cuando esté en la ventana 1
ventana1.type_keys("{ENTER}")





