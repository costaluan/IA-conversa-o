import speech_recognition as sr
import pytesseract

# Apontar para o executável do pytesseract
pytesseract.pytesseract.tesseract_cmd = ('C:\Program Files\Tesseract-OCR\Tesseract.exe')

# Configurando o reconhecedor de fala
recognizer = sr.Recognizer()

# Loop para escutar continuamente o microfone
while True:
    # Captura do áudio do microfone
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = recognizer.listen(source)

    try:
        # Transcrição do áudio em texto usando o Google Web Speech API
        text = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse:", text)
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
    except sr.RequestError as e:
        print("Erro ao requisitar resultados do serviço de reconhecimento de fala; {0}".format(e))