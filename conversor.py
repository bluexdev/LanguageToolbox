from flask import Flask, request, render_template, send_file
from googletrans import Translator
from gtts import gTTS
import io

app = Flask(__name__)

translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        src_lang = request.form['src_lang']
        dest_lang = request.form['dest_lang']
        opcion = request.form['opcion']

        # Validación básica
        if not texto.strip():
            return render_template('index.html', error="Por favor, ingresa un texto.", texto=texto, resultado=None, audio=None)
        
        try:
            if opcion == 'texto':
                # Traducir y mostrar texto
                texto_traducido = translator.translate(texto, src=src_lang, dest=dest_lang).text
                return render_template('index.html', texto=texto, resultado=texto_traducido, audio=None, error=None)

            elif opcion == 'audio':
                # Traducir y generar audio
                texto_traducido = translator.translate(texto, src=src_lang, dest=dest_lang).text
                audio_data = generar_audio(texto_traducido, dest_lang)
                return render_template('index.html', texto=texto, resultado=texto_traducido, audio=audio_data, error=None)

            elif opcion == 'audio_directo':
                # Generar audio sin traducir
                audio_data = generar_audio(texto, src_lang)
                return render_template('index.html', texto=texto, resultado=texto, audio=audio_data, error=None)

        except Exception as e:
            return render_template('index.html', error=f"Error al procesar la solicitud: {str(e)}", texto=texto, resultado=None, audio=None)

    return render_template('index.html', texto=None, resultado=None, audio=None, error=None)

@app.route('/audio')
def serve_audio():
    """Función que sirve el archivo de audio generado dinámicamente."""
    texto = request.args.get('texto')
    lang = request.args.get('lang')
    tts = gTTS(text=texto, lang=lang)
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    # Generar un nombre de archivo basado en el texto
    filename = "audio.mp3"

    # Enviar el archivo con la opción de descarga
    return send_file(audio_file, mimetype='audio/mpeg', as_attachment=True, download_name=filename)

def generar_audio(texto, lang):
    """Genera un enlace temporal para el audio."""
    return f"/audio?texto={texto}&lang={lang}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
