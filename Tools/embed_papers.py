from crewai.tools import tool 
import numpy as np

from fastembed import TextEmbedding
@tool("embed_papers")
def embed_papers(papers: list[str]) -> dict:
    """Generates embeddings for each paper to support similarity search or clustering."""
    embedding_model = TextEmbedding()
    embeddings_generator = embedding_model.embed(papers)
    embeddings_list = list(embeddings_generator)
    return {"status": "success", "embeddings": embeddings_list}


