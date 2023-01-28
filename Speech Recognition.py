import speech_recognition as sr
from text_to_speech import speak

sr_init = sr.Recognizer()


def speechtotext():
    with sr.Microphone() as mic:
        print("\n [ INFO ] Say something ")
        speech_data = sr_init.listen(source=mic, timeout=3)
        speech_text = sr_init.recognize_google(speech_data, language='en-US')
        print(f" [ REPLIED ] You said {speech_text}")
        speak(speech_text)


speechtotext()