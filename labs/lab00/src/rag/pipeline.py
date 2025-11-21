from src.rag.retriever import Retriever

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()

    def run(self, query: str) -> str:
        """
        Run the RAG pipeline.
        """
        docs = self.retriever.retrieve(query)
        # Placeholder for generation logic
        return "RAG Response placeholder"
