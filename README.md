# Generador de Firmas

Este script genera imágenes de firmas a partir de nombres en un archivo CSV.

## Requisitos

- Python 3.x
- pandas
- Pillow (PIL)

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instalar dependencias:
   ```bash
   pip install pandas pillow
   ```

## Uso

1. Preparar un archivo CSV llamado `nombres.csv` con una columna llamada "Nombre"
2. Opcional: Agregar un archivo de fuente TTF llamado `fuente.ttf`
3. Ejecutar el script:
   ```bash
   python script.py
   ```

Las imágenes generadas se guardarán en la carpeta `firmas/`

## Configuración

Puedes modificar los siguientes parámetros en el diccionario `CONFIG` del script:

- `csv_file`: Ruta del archivo CSV
- `output_dir`: Carpeta de salida
- `font_file`: Ruta del archivo de fuente
- `imagen_ancho`: Ancho de la imagen
- `imagen_alto`: Alto de la imagen
- `tamano_fuente`: Tamaño de la fuente
- `color_texto`: Color del texto (RGB)
- `columna_nombre`: Nombre de la columna en el CSV
