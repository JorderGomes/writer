# importações
import download
import conversions
import transcribe
import delete_files
import time
import google.generativeai as gemni
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('API_KEY')

# receber link
link = "https://www.youtube.com/watch?v=kkHJce9-oLE&pp=ygUMYXJpc3TDs3RlbGVz"

start_time = time.time()
# baixar áudio e formata título recebendo o novo título
original_title, output_path, original_file_path = download.download_mp3(link)
formatted_title = download.rename_file(original_file_path)

# converter para wav
wav_path = conversions.convert(formatted_title)

# converter para texto
transcription = transcribe.silence_based_conversion(wav_path) #file.read() # 

# pedir resumo para IA
gemni.configure(api_key=key)
model = gemni.GenerativeModel('gemini-1.5-pro-latest')
prompt = "Por favor resuma este texto e faça o possível para completar as lacunas e dar sentido ao resumo: \n\n"
response = model.generate_content(prompt + transcription).text
print(response)

# apagar arquivos
delete_files.delete()
end_time = time.time()

execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")