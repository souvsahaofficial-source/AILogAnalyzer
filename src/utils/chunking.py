from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_logs(logs : str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=50
    )
    return splitter.split_text(logs)