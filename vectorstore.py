import chromadb
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from loader import load_all_documents

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="chroma_db")
        self.collection = self.client.get_or_create_collection("rag-langchain")
    
    

    def create_chunks(self,documents):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=120)
        chunks = text_splitter.split_documents(documents)
        return chunks
        
    def embed_chunks(self, text):
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        return embeddings.embed_documents(text)
    
    def add_collection(self, documents):
        chunks = self.create_chunks(documents)
        
        for index, chunk in enumerate(chunks):
            embedding = self.embed_chunks(chunks.page_content)
            # print(f"Adding chunk {index} to the collection...")
            # print(embedding)
            # print(chunk.page_content)
            self.collection.add(
                documents=[chunk.page_content],
                embeddings = embedding,
                metadatas = [{"source": chunk.metadata["source"]}],
                ids=[f"{index}"]
            )
            
        print(f"Added {len(chunks)} chunks to the collection successfully")
            
    def query_collection(self, query):
        embedding = self.embed_chunks(query)
        results = self.collection.query(
            query_embeddings = [embedding],
            n_results = 3,
            where = {"embedding": embedding}
        )
        print(f"Total results: {len(results)}")
        return results['documents'][0]
            
    
        