def log_ai_tool_usage(tool_name, details):
    with open("app/logs/ai_tool_usage.log", "a") as f:
        f.write(f"{tool_name}: {details}\n")

def chunk_text(text, chunk_size=512):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
