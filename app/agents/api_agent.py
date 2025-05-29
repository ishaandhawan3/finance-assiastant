import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
from app.config import ALPHA_VANTAGE_KEY
from app.utils import log_ai_tool_usage

class APIAgent:
    def __init__(self):
        self.ts = TimeSeries(key=ALPHA_VANTAGE_KEY, output_format='pandas')

    def get_realtime(self, symbol):
        data, _ = self.ts.get_intraday(symbol, interval='1min')
        log_ai_tool_usage("AlphaVantage", f"Fetched intraday for {symbol}")
        return data.tail(1).to_dict()

    def get_history(self, symbol, period="1mo"):
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period)
        log_ai_tool_usage("YahooFinance", f"Fetched history for {symbol}")
        return hist.tail(5).to_dict()
