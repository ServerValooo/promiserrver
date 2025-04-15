import requests
from tqdm import tqdm  # Para barra de progreso

def descargar_archivo(url, nombre_archivo=None):
    try:
        # Si no se proporciona nombre de archivo, usa el nombre del link
        if not nombre_archivo:
            nombre_archivo = url.split("/")[-1]

        # Hacemos la petición con streaming para descargar por bloques
        respuesta = requests.get(url, stream=True)
        respuesta.raise_for_status()  # Lanza error si la descarga falla

        # Tamaño total del archivo (en bytes)
        total = int(respuesta.headers.get('content-length', 0))
        bloque = 1024  # 1KB

        # Abrimos el archivo en modo escritura binaria y escribimos los datos
        with open(nombre_archivo, 'wb') as archivo, tqdm(
            desc=nombre_archivo,
            total=total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as barra:
            for datos in respuesta.iter_content(chunk_size=bloque):
                archivo.write(datos)
                barra.update(len(datos))

        print(f"Descarga completada: {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso:
url_directo = 'https://mediafilez.forgecdn.net/files/6378/550/ServerFiles-2.42.zip'
descargar_archivo(url_directo)
