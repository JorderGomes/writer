import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.utils import make_chunks


def silence_based_conversion(path):
    video_name = path.split("/")[-1]
    file_rec_name = video_name.split(".")[0]+"_rec.txt"
    
    sound = AudioSegment.from_wav(path)
    chunk_length_ms = 60000
    chunks = make_chunks(sound, chunk_length_ms)
    
    print(os.getcwd())

    os.chdir('assets/texts')
    fh = open(file_rec_name, "w+")
    os.chdir('../')
    
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass
    os.chdir('audio_chunks')

    text = ""

    for i, chunk in enumerate(chunks):
        chunk.export(f"./chunk{i}.wav", format="wav")
        filename = f'chunk{i}.wav'
        
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_listened = r.listen(source)
            try:
                rec = r.recognize_google(audio_listened, language="pt-BR")
                text = text + rec
                fh.write(rec + ". \n")  
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results. Check your internet connection")
    
    os.chdir('../../')
    return text
