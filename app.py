import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# Load environment variables from .env file
load_dotenv()

# Load configuration variables
api_key = os.getenv("API_KEY")
region = os.getenv("REGION")
language = os.getenv("LANGUAGE", "en-US")
output_path = os.getenv("OUTPUT_PATH", "/Users/mahassaf004/Desktop/output.txt")

# Create Flask app
app = Flask(__name__)

# Function to initialize Azure Speech SDK
def initialize_speech_sdk():
    """ Initialize Azure Speech SDK client """
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=False)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    return speech_recognizer

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle file upload
        if 'audio_file' not in request.files:
            return redirect(request.url)
        
        file = request.files['audio_file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            # Save the uploaded file to a temporary location
            file_path = os.path.join(app.root_path, 'uploads', file.filename)
            file.save(file_path)
            
            # Perform speech-to-text conversion
            recognizer = initialize_speech_sdk()
            audio_input = speechsdk.audio.AudioConfig(filename=file_path)
            result = recognizer.recognize_once_async().get()
            transcript = result.text
            
            # Save transcript to output file
            with open(output_path, 'w') as f:
                f.write(transcript)
            
            return redirect(url_for('result'))
    
    return render_template('upload.html')

# Route for result page
@app.route('/result')
def result():
    try:
        # Read from output file
        with open(output_path, 'r') as f:
            transcript = f.read()
        return render_template('result.html', transcript=transcript)
    except FileNotFoundError:
        return "Transcript not found."

if __name__ == '__main__':
    app.run(debug=True)
