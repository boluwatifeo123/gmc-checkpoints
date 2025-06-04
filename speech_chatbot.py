# Create Chatbot.py
import nltk
import streamlit as st
import speech_recognition as sr
import random
import string

# Download NLTK data if not already present
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Sample chatbot pattern-response pairs (can be replaced with file-based logic)
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm fine, thank you.", "Doing well!"]],
    ["what is your name?", ["I'm a chatbot."]],
    ["quit", ["Goodbye!", "See you later!"]],
    [".*", ["Sorry, I didn't understand that."]]
]

chatbot = Chat(pairs, reflections)

# Function to transcribe speech
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your voice.")
        except sr.RequestError:
            st.error("Could not request results from Google Speech Recognition.")
    return None

# Chatbot response function
def get_response(user_input):
    return chatbot.respond(user_input)

# Streamlit UI
def main():
    st.title("🎤 Voice-Enabled Chatbot")

    input_mode = st.radio("Choose your input method:", ("Text", "Speech"))

    user_input = ""

    if input_mode == "Text":
        user_input = st.text_input("You:", "")
    elif input_mode == "Speech":
        if st.button("Start Talking"):
            user_input = transcribe_speech()

    if user_input:
        response = get_response(user_input)
        st.text_area("Chatbot:", value=response, height=100)

if __name__ == "__main__":
    main()
