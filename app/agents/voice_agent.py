import speech_recognition as sr
from TTS.api import TTS
from app.utils import log_ai_tool_usage

class VoiceAgent:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

    def speech_to_text(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio)
            log_ai_tool_usage("SpeechRecognition", "Converted speech to text")
            return text

    def text_to_speech(self, text, output_path="output.wav"):
        self.tts.tts_to_file(text=text, file_path=output_path)
        log_ai_tool_usage
