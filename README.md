# BBB Downloader

Script para descargar y unir los archivos de las clases en BBB generando un video listo para subir.

# Requisitos

- Python 3.11
- FFMPEG

# Uso

El script hace uso de poetry así que se deben instalar las dependencias para
primero

```bash
poetry install
```

Luego se requiere activar el entorno virtual de poetry

```bash
poetry shell
```

Ahora está listo para ejecutar el comando. Se debe agregar una variable de entorno `CODE` con el hash de la grabación.

```bash
CODE=[hash] python main.py
```
