from flask import Flask, render_template, request, jsonify
from google.cloud import texttospeech, speech
import io, base64

app = Flask(__name__)

def text_to_speech(input_text, ssml_gender, speaking_rate):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-ES",
        ssml_gender=ssml_gender
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate = float(speaking_rate)
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    audio_base64 = base64.b64encode(response.audio_content).decode("utf-8")
    return audio_base64

def audio_to_text(audio_content):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000,
        language_code="es-ES"
    )
    response = client.recognize(config=config, audio=audio)
    transcript = " ".join([result.alternatives[0].transcript for result in response.results])
    return transcript

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form['text']

    ssml_gender = request.form['ssml_gender']
    speaking_rate = request.form['speaking_rate']
    print(ssml_gender)

    audio_data = text_to_speech(input_text, ssml_gender, speaking_rate)
    return render_template('index.html', audio_data=audio_data)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio_data = request.files['audio'].read()
    transcript = audio_to_text(audio_data)
    return jsonify({"transcript": transcript})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')