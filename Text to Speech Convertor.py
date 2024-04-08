!pip install SpeechRecognition
!pip install gTTS
!pip install pyaudio


import speech_recognition as sr
from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # This opens the file using the default media player

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def evaluate_accuracy(original_text, recognized_text):
    if recognized_text:
        print(f"Original Text: {original_text}")
        print(f"Recognized Text: {recognized_text}")

        original_words = set(original_text.lower().split())
        recognized_words = set(recognized_text.lower().split())

        common_words = original_words.intersection(recognized_words)
        accuracy = len(common_words) / len(original_words)
        print(f"Accuracy: {accuracy * 100:.2f}%")
    else:
        print("No text recognized. Accuracy cannot be calculated.")

if __name__ == "__main__":
    original_text = "Hello, how are you today?"

    # Convert text to speech
    text_to_speech(original_text)

    # Speech to text
    recognized_text = speech_to_text()

    # Evaluate accuracy
    evaluate_accuracy(original_text, recognized_text)
