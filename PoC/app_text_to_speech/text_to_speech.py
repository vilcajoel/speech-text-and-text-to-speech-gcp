from google.cloud import texttospeech
import io
def text_to_speech(text_file_path, output_audio_path):
    """Convierte texto a audio usando Google Text-to-Speech API y guarda el resultado en un archivo MP3."""
    with io.open(text_file_path, "rb") as text_file:
        input_text = text_file.read()

    client = texttospeech.TextToSpeechClient()

    # Configuración de entrada de texto
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # Configuración de la voz (idioma y género)
    voice = texttospeech.VoiceSelectionParams(
        language_code="es-ES",  # Cambiar a "en-US" para inglés u otro idioma soportado
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Configuración del tipo de audio de salida
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Solicitud a la API de Google Cloud
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # Guardar el audio en un archivo MP3
    with open(output_audio_path, "wb") as audio_file:
        audio_file.write(response.audio_content)

    print(f"Audio guardado en: {output_audio_path}")

if __name__ == "__main__":

    text_file_path = "input.txt"
    output_audio_path = "output.mp3"  # Archivo de salida

    text_to_speech(text_file_path, output_audio_path)
