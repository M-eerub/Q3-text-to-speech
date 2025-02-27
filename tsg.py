import streamlit as st 
from gtts import gTTS
import os

st.title("Text to Speech Generator")

user_input = st.text_area("Write your text here")

language = st.selectbox("Select your language", ["en", "es", "de", "fr", "ar", "ur"])

if st.button("Convert Into Speech"):
    if user_input:
        tts = gTTS(text=user_input, lang=language, slow=False)
        tts.save("Speech.mp3")
        st.audio("Speech.mp3")
    

