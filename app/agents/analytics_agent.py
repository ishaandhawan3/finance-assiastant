import pandas as pd
from app.utils import log_ai_tool_usage

class AnalyticsAgent:
    def calculate_moving_average(self, data, window=5):
        df = pd.DataFrame(data)
        ma = df['close'].rolling(window=window).mean().tolist()
        log_ai_tool_usage("Analytics", "Calculated moving average")
        return ma
