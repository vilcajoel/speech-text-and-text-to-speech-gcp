from google.cloud import speech
import io

def transcribe_mp3(mp3_file_path, output_txt_path):
    """Convierte el audio de un archivo MP3 a texto usando Google Speech-to-Text y lo guarda en un archivo de texto."""

    client = speech.SpeechClient()

    # Leer el archivo MP3
    with io.open(mp3_file_path, "rb") as audio_file:
        content = audio_file.read()

    # Configuración para formato MP3
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,  # Procesar directamente MP3
        sample_rate_hertz=44100,  # Ajusta según la tasa de muestreo de tu archivo
        language_code="es-ES",  # Cambia al idioma deseado
    )

    # Enviar la solicitud a la API de Google Cloud Speech-to-Text
    response = client.recognize(config=config, audio=audio)

    # Guardar el texto en un archivo
    with open(output_txt_path, "w") as txt_file:
        for result in response.results:
            transcript = result.alternatives[0].transcript
            txt_file.write(transcript + "\n")

    print(f"Transcripción guardada en: {output_txt_path}")

if __name__ == "__main__":
    mp3_file_path = "audio.mp3"  # Asegúrate de que el archivo está en el mismo directorio
    output_txt_path = "output.txt"
    transcribe_mp3(mp3_file_path, output_txt_path)
