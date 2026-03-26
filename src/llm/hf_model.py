import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from src.config.settings import HF_TOKEN, MODEL_REPO

def get_llm():
    model = HuggingFaceEndpoint(
        repo_id=MODEL_REPO,
        task="text-generation",
        max_new_tokens=512,
        temperature=0.2,
        huggingfacehub_api_token=HF_TOKEN,
        do_sample=False,
    )
    return ChatHuggingFace(llm=model, verbose=True)