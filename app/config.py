import os
from dotenv import load_dotenv

load_dotenv()

# Ollama local server
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
# Qdrant vector database
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
# Redis for message passing
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
