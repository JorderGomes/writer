import services.summarize as summarize
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
    link = request.get_json()['link']
    response = summarize.transcribe_video(link)
    return {
        'summary': response
    }


if __name__ == '__main__':
    app.run()
