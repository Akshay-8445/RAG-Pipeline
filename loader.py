from langchain_community.document_loaders import PyPDFLoader, TextLoader
from pathlib import Path

def load_all_documents(path, file_type):
    
    path = Path(path)
    directory_path = path.glob("**/*.pdf")
    
    documents = []
    for file in directory_path:
        print("file", file)
        loader = PyPDFLoader(file)
        documents.extend(loader.load())
    return documents

if __name__ == "__main__":
    documents = load_all_documents("data", "pdf")
    print(len(documents))