import os
from dotenv import load_dotenv
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_REPO = "meta-llama/Llama-3.1-8B-Instruct"

