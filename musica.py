from googleapiclient.discovery import build
import yt_dlp as youtube_dl
import os
from flask import Flask, request, send_from_directory

# Configurações
API_KEY = 'YOU_API_KEY' # Coloque sua API aqui
DOWNLOAD_FOLDER = 'downloads'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Inicializa o Flask app
app = Flask(__name__)

# Função para pesquisar o vídeo no YouTube
def search_youtube(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        type='video',
        maxResults=1
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return f'https://www.youtube.com/watch?v={video_id}'

# Função para converter o vídeo em MP3
def download_and_convert(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        return filename

# Endpoint para buscar e converter a música
@app.route('/convert', methods=['GET'])
def convert():
    query = request.args.get('query')
    if not query:
        return "Parâmetro 'query' é necessário", 400
    
    url = search_youtube(query)
    filename = download_and_convert(url)
    return f"Arquivo MP3 disponível em: /downloads/{os.path.basename(filename)}"

# Endpoint para servir arquivos MP3
@app.route('/downloads/<path:filename>', methods=['GET'])
def download(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

# Inicializa a aplicação
if __name__ == '__main__':
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)
    app.run(debug=True, port=5001)  # Atualizado para usar a porta 5001
