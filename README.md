#Local RAG Pipeline with Ollama and ChromaDB

A local Retrieval-Augmented Generation (RAG) application that loads PDF documents, splits them into smaller chunks, creates embeddings with Ollama, stores the vectors in ChromaDB, retrieves relevant content, and generates document-based answers using Llama 3.1.

Features

Loads multiple PDF documents automatically

Splits document content into overlapping chunks

Generates local embeddings with nomic-embed-text

Stores and retrieves vectors using ChromaDB

Generates answers with the local llama3.1 model

Runs locally without requiring a paid API key

Uses a simple command-line interface

RAG Workflow

PDF documents are loaded from Data/PDF_File.

The text is divided into smaller overlapping chunks.

Ollama generates an embedding for each chunk.

ChromaDB stores the chunks and their embeddings.

The user's question is converted into an embedding.

The most relevant document chunks are retrieved.

Llama 3.1 generates an answer using the retrieved context.

Technology Stack
Python 3.11
LangChain
Ollama
Llama 3.1
Nomic Embed Text
ChromaDB
PyPDF

Project Structure

RAG Pipeline/
├── Data/
│   └── PDF_File/
│       ├── Deep_Learning_for_RAG.pdf
│       └── LLMs_and_Embeddings_for_RAG.pdf
├── loader.py
├── main.py
├── prompt.py
├── rag_pipeline.py
├── vectorstore.py
├── requirements.txt
└── README.md




The application displays the following menu:

1. Index the PDF documents
2. Ask a question
3. Exit

Choose option 1 first to index the documents. After indexing finishes, choose option 2 and enter a question.

Add Your Own Documents

Copy PDF files into Data/PDF_File.
Start the application with python main.py.
Select option 1 to index the documents.
Select option 2 to ask questions about them.


Make sure the documents are stored inside:

Data/PDF_File
Empty vector database
Run the application and select option 1 before asking a question.
Privacy and Cost

The language model and embedding model run locally through Ollama. No paid API key is required. The documents remain on the local computer unless the project is deliberately connected to an external service.

##Future Improvements

Add a Streamlit web interface
Support DOCX, TXT, and CSV files
Display document names and page numbers with answers
Add conversation history
Prevent duplicate indexing
Add document upload and database-reset controls


### RAG Question and Answer

![RAG Query Result]<img width="1920" height="1200" alt="Screenshot 2026-09-19 193235" src="https://github.com/user-attachments/assets/50907bf5-ea19-44a3-a2f6-04af0e41c191" />

Author

Akshay Pal
B.Tech Computer Science and Engineering (Artificial Intelligence)

License

This project is intended for learning and educational use.#
