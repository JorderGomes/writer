from pydub import AudioSegment
import speech_recognition as sr

def get_name(path):
    file_name = path.split("/")[-1]
    file_name = file_name.split(".")[0]
    return file_name

def mp3towav(path):
    src = path
    name = get_name(path)
    name = "../assets/audio/"+name+".wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(name, format="wav")
    file_audio = sr.AudioFile(name)  
    return name

def convert(file_path):
    return mp3towav(file_path)

