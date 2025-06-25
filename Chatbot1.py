import openai
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🎤 Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# 🎛️ Set TTS voice and speed (optional)
tts.setProperty('rate', 170)

# 🧠 Chat history
messages = [{"role": "system", "content": "You are a helpful assistant."}]

def speak(text):
    print("🤖:", text)
    tts.say(text)
    tts.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Sorry, speech service is unavailable.")
    return None

def chat():
    speak("Hello! I'm your AI Assistant. Say 'exit' to quit.")
    while True:
        user_input = listen()
        if user_input is None:
            continue
        if user_input.lower() == "exit":
            speak("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # ✅ Use GPT-3.5 here
                messages=messages
            )
            reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})
            speak(reply)
        except Exception as e:
            speak("Something went wrong.")
            print("❌ Error:", e)

if __name__ == "__main__":
    chat()

