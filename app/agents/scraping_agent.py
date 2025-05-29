import requests
from bs4 import BeautifulSoup
from app.utils import log_ai_tool_usage

class ScrapingAgent:
    def scrape_news(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        headline = soup.find("h1").text if soup.find("h1") else ""
        article = soup.find("article")
        content = article.text if article else ""
        log_ai_tool_usage("WebScraping", f"Scraped {url}")
        return {"headline": headline, "content": content, "url": url}
