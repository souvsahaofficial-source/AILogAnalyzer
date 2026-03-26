import streamlit as st
from src.rag.rag_pipeline import RAGPipeline

st.set_page_config(page_title="AI Log Analyzer")

st.title("🧠 AI-Powered Log Analyzer")

logs = st.text_area("Paste Logs Here", height=300)
query = st.text_input("Ask a question (optional)")

if st.button("Analyze Logs"):

    if not logs.strip():
        st.warning("Please enter logs")
    else:
        with st.spinner("Analyzing..."):
            pipeline = RAGPipeline()
            result = pipeline.run(logs, query)

            st.subheader("📊 Analysis Result")
            st.text(result)