import streamlit as st
from src.rag.rag_pipeline import RAGPipeline

st.set_page_config(page_title="AI Log Analyzer")

st.title("🧠 AI-Powered Log Analyzer")

# ✅ Persist pipeline
if "pipeline" not in st.session_state:
    st.session_state.pipeline = RAGPipeline()

pipeline = st.session_state.pipeline

uploaded_file = st.file_uploader("Upload Log File", type=["txt", "log"])
logs_input = st.text_area("Or Paste Logs", height=250)
query = st.text_input("Ask a question")

logs = ""

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8")
elif logs_input:
    logs = logs_input

if st.button("Analyze Logs"):
    if not logs.strip():
        st.warning("Please provide logs")
    else:
        with st.spinner("Analyzing..."):
            result = pipeline.run(logs, query)

            st.subheader("📊 Analysis Result")
            st.success("Analysis Completed")
            st.markdown(result)