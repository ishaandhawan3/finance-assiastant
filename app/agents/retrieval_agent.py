from app.vectorstore.vectorstore_agent import VectorStoreAgent
from app.utils import log_ai_tool_usage

class RetrievalAgent:
    def __init__(self):
        self.vectorstore = VectorStoreAgent()

    def retrieve(self, query_embedding):
        results = self.vectorstore.query(query_embedding)
        log_ai_tool_usage("VectorStore", "Queried vector DB")
        return results
