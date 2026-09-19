from prompt import get_prompt
from vectorstore import VectorStore
import ollama

class RAGPipeline:
    def __init__(self):
        self.vectorstore = VectorStore()
        
    def get_relevant_documents(self, query):
        results = self.vectorstore.query_collection(query)
        prompt = get_prompt(results, query)
        response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": prompt }])
        
        return results
    
    
    
    