import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def validar_archivos(csv_path: str, font_path: str) -> bool:
    """
    Valida que los archivos necesarios existan.
    
    Args:
        csv_path: Ruta al archivo CSV
        font_path: Ruta al archivo de fuente
    
    Returns:
        bool: True si los archivos existen, False en caso contrario
    """
    if not os.path.exists(csv_path):
        print(f"Error: El archivo CSV '{csv_path}' no existe.")
        return False
    if not os.path.exists(font_path):
        print(f"Error: El archivo de fuente '{font_path}' no existe.")
        return False
    return True

def generar_firmas(
    csv_path: str,
    output_folder: str,
    font_path: str,
    imagen_ancho: int = 400,
    imagen_alto: int = 100,
    tamano_fuente: int = 45,
    color_texto: tuple = (0, 0, 0),
    columna_nombre: str = "Nombre"
) -> None:
    """
    Genera imágenes de firmas a partir de nombres en un CSV.
    
    Args:
        csv_path: Ruta al archivo CSV con los nombres
        output_folder: Carpeta donde se guardarán las imágenes
        font_path: Ruta al archivo de fuente
        imagen_ancho: Ancho de la imagen en píxeles
        imagen_alto: Alto de la imagen en píxeles
        tamano_fuente: Tamaño de la fuente
        color_texto: Color del texto en RGB
        columna_nombre: Nombre de la columna que contiene los nombres
    """
    if not validar_archivos(csv_path, font_path):
        return

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)
    
    try:
        # Leer el archivo CSV
        df = pd.read_csv(csv_path)
        
        # Validar que exista la columna de nombres
        if columna_nombre not in df.columns:
            print(f"Error: La columna '{columna_nombre}' no existe en el CSV.")
            return
            
        # Cargar la fuente
        try:
            font = ImageFont.truetype(font_path, tamano_fuente)
        except Exception as e:
            print(f"Error al cargar la fuente: {e}")
            print("Usando fuente por defecto...")
            font = ImageFont.load_default()
        
        for index, row in df.iterrows():
            nombre = row[columna_nombre].strip()
            if not nombre:
                print(f"Advertencia: Nombre vacío en la fila {index + 1}")
                continue
                
            # Crear imagen en blanco
            img = Image.new("RGBA", (imagen_ancho, imagen_alto), (255, 255, 255, 0))
            draw = ImageDraw.Draw(img)
            
            # Dibujar la firma
            draw.text((20, 25), nombre, fill=color_texto, font=font)
            
            # Guardar la imagen
            file_path = os.path.join(output_folder, f"{nombre.replace(' ', '_')}.png")
            img.save(file_path)
        
        print("Firmas generadas correctamente.")
        
    except pd.errors.EmptyDataError:
        print("Error: El archivo CSV está vacío.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Configuración
CONFIG = {
    "csv_file": "nombres.csv",
    "output_dir": "firmas",
    "font_file": "fuente.ttf",
    "imagen_ancho": 400,
    "imagen_alto": 100,
    "tamano_fuente": 45,
    "color_texto": (0, 0, 0),
    "columna_nombre": "Nombre"
}

if __name__ == "__main__":
    generar_firmas(
        csv_path=CONFIG["csv_file"],
        output_folder=CONFIG["output_dir"],
        font_path=CONFIG["font_file"],
        imagen_ancho=CONFIG["imagen_ancho"],
        imagen_alto=CONFIG["imagen_alto"],
        tamano_fuente=CONFIG["tamano_fuente"],
        color_texto=CONFIG["color_texto"],
        columna_nombre=CONFIG["columna_nombre"]
    )
