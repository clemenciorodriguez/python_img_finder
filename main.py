from flask import Flask
from flask import request
from flask import render_template, jsonify
from bing_image_downloader import downloader
import os
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

files = []



@app.route("/input",  methods=['POST', 'GET'])
def memes():
    # Keyword for image search
      
      query = request.args.get('query', '')
      host_name = os.getcwd()
      print(f'{host_name}')
      # Download images using the library
      response = downloader.download(query, limit=6, output_dir='downloaded_images', adult_filter_off=True, force_replace=False, timeout=60)

      # Ruta de la carpeta que contiene las imágenes
      folder_path = f'./downloaded_images/{query}'
      
      # Obtener la lista de archivos en la carpeta
      file_list = os.listdir(folder_path)
      for f in file_list:
              files.append(f'{host_name}/downloaded_images/{query}/{f}')
      return  files 
      




@app.route('/termino')
def terminado():
    return json.dumps(files)


@app.route('/chekear')
def data():
    return render_template("send.html")
   




      


if __name__ == '__main__':
    app.run(debug=True)