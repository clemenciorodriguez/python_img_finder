from bing_image_downloader import downloader
import os


# Keyword for image search
query = 'cute cats memes'
host_name = os.getcwd()
print(f'{host_name}')
# Download images using the library
response = downloader.download(query, limit=6, output_dir='downloaded_images', adult_filter_off=True, force_replace=False, timeout=60)

# Ruta de la carpeta que contiene las imágenes
folder_path = f'./downloaded_images/{query}'

# Obtener la lista de archivos en la carpeta
file_list = os.listdir(folder_path)

for f in file_list:
    print(f'{host_name}/downloaded_images/{query}/{f}')

print(file_list)
# Iterar sobre los archivos en la carpeta












