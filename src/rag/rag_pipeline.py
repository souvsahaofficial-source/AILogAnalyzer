from src.utils.chunking import split_logs
from src.embeddings.embedding_model import get_embeddings
from src.vectorstore.faiss_store import create_vector_store, get_retriever
from src.llm.hf_model import get_llm
from src.rag.prompt import RAG_PROMPT

class RAGPipeline:

    def __init__(self):
        self.embeddings = get_embeddings()
        self.llm = get_llm()

    def run(self, logs, query=None):
        chunks = split_logs(logs)

        vectorstore = create_vector_store(chunks, self.embeddings)
        retriever = get_retriever(vectorstore)

        docs = retriever.invoke(query if query else logs)

        context = "\n".join([doc.page_content for doc in docs])

        final_prompt = f"""
{RAG_PROMPT}

LOG CONTEXT:
{context}

USER QUESTION:
{query if query else "Analyze logs"}
"""

        response = self.llm.invoke(final_prompt)
        return response.content