import speech_recognition as sr

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")

        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5)

    try:
        # Use PocketSphinx speech recognition engine with 'en-in' language
        text = recognizer.recognize_sphinx(audio, language='en-in')
        print("You said:", text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from PocketSphinx; {0}".format(e))

if __name__ == "__main__":
    recognize_speech()
