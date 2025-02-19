import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

def generar_firmas(csv_path, output_folder, font_path):
    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)
    
    # Leer el archivo CSV
    df = pd.read_csv(csv_path)
    
    for index, row in df.iterrows():
        nombre = row["Nombre"]  # Suponiendo que la columna se llama "Nombre"
        
        # Crear imagen en blanco
        img = Image.new("RGBA", (400, 100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype(font_path, 45)
        except:
            font = ImageFont.load_default()
        
        # Dibujar la firma
        draw.text((20, 25), nombre, fill=(0, 0, 0), font=font)
        
        # Guardar la imagen
        file_path = os.path.join(output_folder, f"{nombre.replace(' ', '_')}.png")
        img.save(file_path)
    
    print("Firmas generadas correctamente.")

# Configuración
csv_file = "nombres.csv"  # Ruta del CSV
output_dir = "firmas"  # Carpeta de salida
font_file = "fuente.ttf"  # Ruta de la fuente

generar_firmas(csv_file, output_dir, font_file)
