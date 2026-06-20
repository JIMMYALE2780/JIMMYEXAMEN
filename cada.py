import os
import time
import names
from colorama import Fore, Style, init
from tqdm import tqdm

# Inicializar colorama para los colores en la terminal
init(autoreset=True)

print(Fore.MAGENTA + Style.BRIGHT + "=== CONFIGURACIÓN DEL SCRIPT ===")

# 1. Solicitar la Ruta del Archivo de Nombres
ruta_archivo = input(Fore.CYAN + "1. Introduce la Ruta del Archivo de Nombres: ")

# 2. Solicitar el Nombre que le daremos
nombre_proyecto = input(Fore.CYAN + "2. Introduce el Nombre que le daremos: ")

# 3. Solicitar la Longitud de las contraseñas
while True:
    try:
        longitud_pass = int(input(Fore.CYAN + "3. Introduce la Longitud de las contraseñas: "))
        break
    except ValueError:
        print(Fore.RED + "Por favor, introduce un número válido.")

print("\n" + Fore.YELLOW + "Esperando que Termux haga su Magia...")

# Simulación de proceso con la barra de progreso tqdm
for i in tqdm(range(100), desc="Procesando", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
    time.sleep(0.03)

# 4. El resultado se guardará automáticamente en la ruta especificada
ruta_destino_base = "/storage/emulated/0/Termux"

# Validamos si la ruta existe, si no, se guarda en el directorio actual para evitar caídas
if os.path.exists(ruta_destino_base):
    ruta_final = os.path.join(ruta_destino_base, f"{nombre_proyecto}_resultado.txt")
else:
    ruta_final = f"{nombre_proyecto}_resultado.txt"

with open(ruta_final, "w", encoding="utf-8") as f:
    f.write(f"Proyecto: {nombre_proyecto}\n")
    f.write(f"Ruta origen: {ruta_archivo}\n")
    f.write(f"Longitud configurada: {longitud_pass}\n")
    f.write("\n--- Nombres Aleatorios Generados de Muestra ---\n")
    for _ in range(5):
        f.write(f"{names.get_full_name()}\n")

print(Fore.GREEN + Style.BRIGHT + f"\n¡Listo! El resultado se ha guardado con éxito en:\n{ruta_final}")
