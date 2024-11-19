# import sys
import pytubefix
import speech_recognition as sr
import subprocess
import transcribe
import delete_files
import google.generativeai as gemni
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('API_KEY')

def transcribe_video(url):
    #download
    yt = pytubefix.YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    output = "audio.mp4"  # Nome do arquivo de saída
    os.chdir("../assets/audio")
    audio.download(filename=output)
    output = f"{output}.m4a"
    output_file = "audio.wav"
    subprocess.call(["ffmpeg", "-i", output, output_file])
    if os.path.exists(output):
        os.remove(output)
    
    os.chdir("../../")
    output_file = "assets/audio/audio.wav"
    transcript = transcribe.silence_based_conversion(output_file)

    #summarize
    gemni.configure(api_key=key)
    model = gemni.GenerativeModel('gemini-1.5-pro-latest')
    prompt = "Por favor resuma este texto e faça o possível para completar as lacunas e dar sentido ao resumo, não faça comentários apenas resuma e corrija as lacunas: \n\n"
    response = model.generate_content(prompt + transcript).text
    
    delete_files.delete_all()
    print(response)
    return response

transcribe_video("https://www.youtube.com/watch?v=kkHJce9-oLE&pp=ygUMYXJpc3TDs3RlbGVz")