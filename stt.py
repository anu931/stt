import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Using Google Web Speech API
        print(f"Original Text: {text}")

        # Get the target language from the user
        target_language = input("Enter the language code to translate to (e.g., 'en' for English, 'hi' for Hindi, 'fr' for French, 'mr' for Marathi, 'de' for German): ")

        # Initialize the translator with the target language
        translator = Translator(to_lang=target_language)

        # Translate the text to the target language
        translated_text = translator.translate(text)
        print(f"Translated Text ({target_language}): {translated_text}")

        # Convert the translated text to speech
        tts = gTTS(text=translated_text, lang=target_language, slow=False)
        tts.save("translated_output.mp3")

        # Play the audio file (works on most systems)
        os.system("start translated_output.mp3")  # For Windows
        # os.system("afplay translated_output.mp3")  # For macOS
        # os.system("mpg321 translated_output.mp3")  # For Linux

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    speech_to_text()
