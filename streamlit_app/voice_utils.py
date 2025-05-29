import requests
import streamlit as st

API_URL = "http://localhost:8000"

def text_to_speech(text):
    r = requests.post(f"{API_URL}/text-to-speech", params={"text": text})
    audio_path = r.json()["audio_path"]
    with open(audio_path, "rb") as f:
        st.audio(f.read())
