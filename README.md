# Proyecto GCP: Conversión de Texto a Audio y Audio a Texto con Google Cloud

Este es un proyecto creado en Google Cloud con el cual mediante una aplicación web desarrollada en **Flask** nos permite la conversión de texto a audio utilizando la API de Google Cloud Text-to-Speech, así como la transcripción de audio a texto con la API de Google Cloud Speech-to-Text.

**⚠️ Importante:** Este proyecto debe ejecutarse exclusivamente en el entorno de **Cloud Shell** de Google Cloud para garantizar la correcta instalación de dependencias y acceso a las credenciales de servicio.


![App Screenshot](https://github.com/vilcajoel/speech-text-and-text-to-speech-gcp/blob/main/WebApp.png?raw=true)

---

## 🚀 Características

- Convierte texto a audio en formato MP3.
- Permite personalizar la voz con opciones de género y velocidad de habla.
- Transcribe audio en español a texto.
- Interfaz web intuitiva con controles de grabación y reproducción de audio.

---

## 🛠️ Requisitos previos

Antes de ejecutar la aplicación, asegúrate de tener los siguientes requisitos instalados en tu entorno de Cloud Shell:

1. **Python 3.11 o superior** (preinstalado en Cloud Shell)
2. **Cuenta de Google Cloud** con las APIs habilitadas:
    - [Text-to-Speech API](https://console.cloud.google.com/marketplace/product/google/texttospeech.googleapis.com)
    ```gcloud services enable texttospeech.googleapis.com```
    - [Speech-to-Text API](https://console.cloud.google.com/marketplace/product/google/speech.googleapis.com)
    ```gcloud services enable speech.googleapis.com```

3. **Dependencias del sistema:** `ffmpeg` (Se instalará en el siguiente paso)

---

## ⚙️ Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en Cloud Shell:

### 1. Clonar el repositorio

```bash
git clone https://github.com/vilcajoel/speech-text-and-text-to-speech-gcp.git
cd speech-text-and-text-to-speech-gcp
```

### 2. Crear un entorno virtual

Crea y activa un entorno virtual para aislar las dependencias del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias del sistema

Ejecuta el siguiente comando para instalar **ffmpeg**, necesario para el procesamiento de audio:

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg
```

### 4. Instalar dependencias de Python

Instala las dependencias necesarias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Contenido de `requirements.txt`:**

```
Flask==3.0.0
google-cloud-texttospeech==2.14.1
google-cloud-speech==2.21.0
gunicorn==21.2.0
```


### 5. Ejecutar la aplicación

Inicia la aplicación Flask con el siguiente comando:

```bash
python app.py
```

La aplicación estará disponible en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Uso de la aplicación

1. **Conversión de Texto a Audio:**
    - Escribe el texto en el cuadro de texto.
    - Selecciona el género de la voz (Neutral, Masculina o Femenina).
    - Ajusta la velocidad de la voz.
    - Haz clic en "Convertir a Audio" y escucha la reproducción.

2. **Conversión de Audio a Texto:**
    - Presiona el botón "Iniciar Grabación".
    - Graba tu voz y presiona "Detener Grabación".
    - Obtén la transcripción en pantalla.

---

## 📂 Estructura del proyecto

```
.
├── app.py
├── requirements.txt
├── templates
│   └── index.html
├── Poc
│   └── app_speech_to_text
│   └── app_text_to_speech
└── README.md
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación, por favor, haz un fork del repositorio y envía un pull request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 📞 Contacto

Para preguntas o sugerencias, contáctame en:
- ✉️ Email: joelvilcatarazona@gmail.com
- 🔗 LinkedIn: [https://www.linkedin.com/in/joelvilca/](https://www.linkedin.com/in/joelvilca/)
- 🐙 GitHub: [https://github.com/vilcajoel](https://github.com/vilcajoel)

---

¡Espero que disfrutes usando esta aplicación! 🚀

