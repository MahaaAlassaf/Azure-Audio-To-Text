from flask import Flask, request, render_template, redirect, url_for, jsonify, send_file
import os
import sys
import time
import azure.cognitiveservices.speech as speechsdk
from werkzeug.utils import secure_filename

# Initialize the Flask app
app = Flask(__name__)

API_Key = "1626e47dfe994fdeb61fa153aa83fa4a"
Region = "eastus"
Output_Path = "/Users/mahassaf004/Desktop/output.txt"
Language = "en-US"

# Configuration check function
def check_configuration(overwrite: bool, input_path: str) -> None:
    required_vars = [API_Key, Region, input_path, Output_Path, Language]
    
    if not all(required_vars):
        sys.exit("Missing configuration parameter.")
    if os.path.isfile(Output_Path) and not overwrite:
        if input(f"Specified output file already exists: {Output_Path}. Overwrite? (yes/no): ").lower() != 'yes':
            sys.exit(1)

# Setup speech recognizer
def setup_speech_recognizer(input_path: str) -> speechsdk.SpeechRecognizer:
    speech_config = speechsdk.SpeechConfig(subscription=API_Key, region=Region, speech_recognition_language=Language)
    audio_config = speechsdk.AudioConfig(filename=input_path)
    return speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Recognize speech from audio file
def recognize_speech(speech_recognizer: speechsdk.SpeechRecognizer) -> list:
    done = False
    all_results = []

    def stop_callback(evt):
        nonlocal done
        speech_recognizer.stop_continuous_recognition()
        done = True
        if evt.result.reason == speechsdk.ResultReason.Canceled:
            details = evt.result.cancellation_details
            if details.reason == speechsdk.CancellationReason.Error:
                print(f"Error code: {details.error_code}\nError details: {details.error_details}")

    speech_recognizer.recognized.connect(lambda evt: all_results.append(evt.result.text))
    speech_recognizer.session_stopped.connect(stop_callback)
    speech_recognizer.canceled.connect(stop_callback)

    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(2)

    return all_results

# Write recognized text to file
def write_text_to_file(text_results: list) -> None:
    try:
        with open(Output_Path, "w", encoding="utf-8") as output:
            output.write("\n".join(text_results))
        print(f"Printed text to {Output_Path}")
    except Exception as e:
        print(f"Could not write text into {Output_Path}\n{e}")

# Route for home page and upload
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            input_path = os.path.join('/tmp', secure_filename(file.filename))
            file.save(input_path)
            check_configuration(True, input_path)
            speech_recognizer = setup_speech_recognizer(input_path)
            text_results = recognize_speech(speech_recognizer)
            write_text_to_file(text_results)
            return redirect(url_for('show_result'))
    return render_template('upload.html')

# Route for showing result
@app.route('/result')
def show_result():
    with open(Output_Path, 'r') as file:
        content = file.read()
    return render_template('result.html', content=content)

# Route for downloading text file
@app.route('/download')
def download_file():
    return send_file(Output_Path, as_attachment=True)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
