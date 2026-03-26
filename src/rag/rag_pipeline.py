from src.utils.chunking import split_logs
from src.embeddings.embedding_model import get_embeddings
from src.vectorstore.faiss_store import create_vector_store, get_retriever
from src.llm.hf_model import get_llm
from src.rag.prompt import RAG_PROMPT

from src.correlation.log_correlation import correlate_logs
from src.scoring.alert_scoring import calculate_alert_score, get_severity

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

        correlation = correlate_logs(chunks)
        score = calculate_alert_score(correlation)
        severity = get_severity(score)

        extra_context = f"""
        ALERT SCORE: {score}
        SEVERITY: {severity}
        TOP ISSUES: {correlation['top_patterns']}
        """

        final_prompt = f"""
{RAG_PROMPT}

SYSTEM ANALYSIS:
{extra_context}

LOG CONTEXT:
{context}

USER QUESTION:
{query if query else "Analyze logs"}
"""

        response = self.llm.invoke(final_prompt)
        return response.content
