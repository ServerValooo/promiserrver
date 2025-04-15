import zipfile
import os

def descomprimir_zip(ruta_zip, ruta_destino=None):
    try:
        if not ruta_destino:
            # Si no se especifica destino, usa el mismo directorio del ZIP
            ruta_destino = os.path.splitext(ruta_zip)[0]

        # Crea el directorio de destino si no existe
        os.makedirs(ruta_destino, exist_ok=True)

        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(ruta_destino)
            print(f"Archivo descomprimido en: {ruta_destino}")
    except zipfile.BadZipFile:
        print("El archivo no es un .zip válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso:
ruta_zip = '/workspaces/REpoValooo/ServerFiles-2.42.zip'  # Cambia esto por la ruta a tu archivo ZIP
descomprimir_zip(ruta_zip)
