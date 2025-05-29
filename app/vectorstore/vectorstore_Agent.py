from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import numpy as np
from app.config import QDRANT_HOST, QDRANT_PORT
from app.utils import log_ai_tool_usage

class VectorStoreAgent:
    def __init__(self, collection="financial_docs"):
        self.client = QdrantClient(QDRANT_HOST, port=QDRANT_PORT)
        self.collection = collection
        self.client.recreate_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE)
        )

    def store(self, docs, embeddings):
        points = [
            {"id": i, "vector": emb.tolist(), "payload": {"text": doc}}
            for i, (doc, emb) in enumerate(zip(docs, embeddings))
        ]
        self.client.upsert(collection_name=self.collection, points=points)
        log_ai_tool_usage("Qdrant", "Stored embeddings")

    def query(self, query_embedding):
        results = self.client.search(
            collection_name=self.collection,
            query_vector=query_embedding.tolist(),
            limit=3
        )
        log_ai_tool_usage("Qdrant", "Queried embeddings")
        return results
