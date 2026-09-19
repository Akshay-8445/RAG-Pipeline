from langchain_core.prompts import PromptTemplate

def get_prompt(context, query):
    prompt ="""
    You are a helpful assistant that can answer questions about the documents.
    you are given a question and a context.
    you need to answer then question based on the context.
    Context :
    {context}
    Question :
    {query} 
    Answer:
    """
    
    return prompt;

if __name__ == "__main__":
    context = "The capital of France is Paris."
    query = "What is the capital of France?"
    prompt = get_prompt(context, query)
    print(prompt)