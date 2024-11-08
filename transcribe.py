import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.utils import make_chunks

path = "assets/audio/grandespensadoresaristteles.wav"

def silence_based_conversion(path):
    # Define o nome do arquivo de saída com base no nome do arquivo de entrada
    video_name = path.split("/")[-1]
    file_rec_name = video_name.split(".")[0]+"_rec.txt"
    
    # Carrega o áudio e o divide em fragmentos de 60 segundos
    sound = AudioSegment.from_wav(path)
    chunk_length_ms = 60000
    chunks = make_chunks(sound, chunk_length_ms)
    
    os.chdir('assets/texts')
    fh = open(file_rec_name, "w+")
    os.chdir('../')
    
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass
    os.chdir('audio_chunks')
    
    for i, chunk in enumerate(chunks):
        # Exporta cada fragmento como arquivo WAV
        chunk.export(f"./chunk{i}.wav", format="wav")
        filename = f'chunk{i}.wav'
        
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_listened = r.listen(source)
            try:
                rec = r.recognize_google(audio_listened, language="pt-BR")
                fh.write(rec + ". \n")  # Grava a transcrição
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results. Check your internet connection")
    
    os.chdir('..')

silence_based_conversion(path)