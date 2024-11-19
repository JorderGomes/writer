import services.summarize as summarize
from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
load_dotenv()
key = os.getenv('API_KEY')

UPLOAD_FOLDER = 'assets/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/alive', methods=['GET'])
def alive():
	return {
		'message':'writer api is live'
	}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/write-image', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})
    file = request.files['file']  

    # Verifica se o arquivo foi selecionado
    if file.filename == '':
        return jsonify({'message': 'No selected file'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully',  
 'filename': filename})
    return jsonify({'message': 'Allowed file types are png, jpg, jpeg, gif'})


@app.route('/summarize-video', methods=['POST'])
def summarize_video():
    link = request.get_json()['link']
    response = summarize.transcribe_video(link)
    return {
        'summary': response
    }


if __name__ == '__main__':
    app.run()
