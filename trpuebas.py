import os
from glob import glob
import platform

def collect_files(base_folders, dest_folder):
    """
    Recopila archivos PNG y GIF desde las carpetas base especificadas
    y los prepara para el comando de PyInstaller.
    """
    data_files = []
    for base_folder in base_folders:
        # Busca archivos PNG y GIF en la carpeta base
        png_files = glob(f'{base_folder}/**/*.png', recursive=True)
        gif_files = glob(f'{base_folder}/**/*.gif', recursive=True)
        
        for file in png_files + gif_files:
            folder_name = os.path.basename(base_folder)
            # Prepara la ruta de destino para cada archivo
            dest_path = os.path.join(dest_folder, folder_name, os.path.relpath(file, base_folder))
            dest_dir = os.path.dirname(dest_path)
            # Crea el directorio de destino si no existe
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            data_files.append((file, dest_dir))

    return data_files

# Lista de carpetas a buscar
base_folders = ['razas', 'iconos', 'fondos', 'armas', 'gif']
dest_folder = 'data'

# Archivo de icono
icon_path = 'iconos/icono_app.png'

# Si el archivo de icono no existe, puedes omitir esta opción en el comando de PyInstaller
if not os.path.isfile(icon_path):
    icon_path = None
    print(f"El archivo de icono {icon_path} no se encuentra. Se omite el ícono en el comando de PyInstaller.")

# Genera el comando de PyInstaller
separator = ';' if platform.system() == 'Windows' else ':'
pyinstaller_command = "pyinstaller --onefile --noconsole "
if icon_path:
    pyinstaller_command += f"--icon={icon_path} "

# Añade todos los archivos PNG y GIF al comando de PyInstaller
data_files = collect_files(base_folders, dest_folder)
for src, dst in data_files:
    pyinstaller_command += f"--add-data \"{src}{separator}{dst}\" "

# Añade el archivo principal al comando
pyinstaller_command += "main.py"

# Imprime el comando para verificación
print(f"Ejecutando comando: {pyinstaller_command}")

# Ejecuta el comando
os.system(pyinstaller_command)
