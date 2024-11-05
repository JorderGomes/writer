from pydub import AudioSegment
import speech_recognition as sr

def get_name(path):
    # Extrai o nome do arquivo (sem extensão) do caminho
    file_name = path.split("/")[-1]
    file_name = file_name.split(".")[0]
    return file_name

def mp3towav(path):
    src = path
    name = get_name(path)
    name = "ignored-files/audio/"+name+".wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(name, format="wav")
    file_audio = sr.AudioFile(name)  

def convert(file_path):
    mp3towav(file_path)

file_path = "ignored-files/audio/grandespensadoresaristteles.mp3"
convert(file_path)