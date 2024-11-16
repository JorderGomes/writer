import services.download as download
import services.conversions as conversions
import services.transcribe as transcribe
import services.delete_files as delete_files
import google.generativeai as gemni
from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
load_dotenv()
key = os.getenv('API_KEY')

@app.route('/alive', methods=['GET'])
def alive():
	return {
		'message':'writer api is live'
	}

@app.route('/summarize-video', methods=['POST'])
def summarize_video():
    # baixar áudio e formata título recebendo o novo título
    link = request.get_json().link
    original_title, output_path, original_file_path = download.download_mp3(link)
    formatted_title = download.rename_file(original_file_path)
    
    # converter para wav
    wav_path = conversions.convert(formatted_title)
    
    # converter para texto
    transcription = transcribe.silence_based_conversion(wav_path) #file.read() # 
    
    # pedir resumo para IA
    gemni.configure(api_key=key)
    model = gemni.GenerativeModel('gemini-1.5-pro-latest')
    prompt = "Por favor resuma este texto e faça o possível para completar as lacunas e dar sentido ao resumo, não faça comentários apenas resuma e corrija as lacunas: \n\n"
    response = model.generate_content(prompt + transcription).text

    # apagar arquivos
    delete_files.delete_all()
    return {
        'summary': response
    }

if __name__ == '__main__':
    app.run()
