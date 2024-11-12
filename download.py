import yt_dlp
import os
import re

# https://www.youtube.com/watch?v=kkHJce9-oLE&pp=ygUMYXJpc3TDs3RlbGVz

def download_mp3(url, output_path="assets/audio/"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    return info['title'], output_path, ydl.prepare_filename(info).replace(".webm", ".mp3")

def rename_file(original_file_path):
    # Extrai o nome do arquivo a partir do caminho completo
    original_title = os.path.basename(original_file_path).replace(".mp3", "")
    formatted_title = "_".join(original_title.lower().split())
    formatted_title = re.sub(r'[^a-zA-Z0-9\s]', '', formatted_title)
    formatted_file_path = os.path.join(os.path.dirname(original_file_path), f"{formatted_title}.mp3")

    os.rename(original_file_path, formatted_file_path)
    return "assets/audio/" + formatted_title + ".mp3"

# Uso das funções
# url = input("Escreva a URL do vídeo: \n>> ")
# original_title, output_path, original_file_path = download_mp3(url)
# formatted_title = rename_file(original_file_path)

# print(f"{original_title} has been successfully downloaded as {formatted_title}.")