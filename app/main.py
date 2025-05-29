from fastapi import FastAPI, UploadFile
from app.agents.api_agent import APIAgent
from app.agents.scraping_agent import ScrapingAgent
from app.agents.analytics_agent import AnalyticsAgent
from app.agents.llm_agent import LLMAgent
from app.agents.voice_agent import VoiceAgent

app = FastAPI(title="Finance Assistant API")

api_agent = APIAgent()
scraping_agent = ScrapingAgent()
analytics_agent = AnalyticsAgent()
llm_agent = LLMAgent()
voice_agent = VoiceAgent()

@app.get("/price/{symbol}")
def get_price(symbol: str):
    return api_agent.get_realtime(symbol)

@app.get("/history/{symbol}")
def get_history(symbol: str):
    return api_agent.get_history(symbol)

@app.post("/scrape")
def scrape_news(url: str):
    return scraping_agent.scrape_news(url)

@app.post("/analyze")
def analyze(data: dict):
    return analytics_agent.calculate_moving_average(data)

@app.post("/brief")
async def generate_brief(context: str):
    brief_text = await llm_agent.generate_brief(context)
    return {"brief": brief_text}

@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile):
    text = voice_agent.speech_to_text(file.file)
    return {"text": text}

@app.post("/text-to-speech")
def text_to_speech(text: str):
    path = voice_agent.text_to_speech(text)
    return {"audio_path": path}
