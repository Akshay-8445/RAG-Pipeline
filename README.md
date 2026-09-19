# RAG with LangChain + Ollama

Local RAG pipeline using LangChain, ChromaDB, Ollama embeddings (`nomic-embed-text`) and Llama 3.1.

## Windows / PyCharm setup

1. Install Python 3.11 and Ollama.
2. Open this project folder in PyCharm.
3. Open the PyCharm terminal and create a fresh environment:
   `py -3.11 -m venv .venv`
4. Activate it in PowerShell:
   `.\.venv\Scripts\Activate.ps1`
5. Upgrade pip:
   `python -m pip install --upgrade pip`
6. Install packages:
   `pip install -r requirements.txt`
7. Download the two Ollama models:
   `ollama pull nomic-embed-text`
   `ollama pull llama3.1`
8. Make sure Ollama is running. If needed, run `ollama serve` in a separate terminal.
9. Put one or more PDF files inside the `data` folder.
10. Start the project:
   `python main.py`
11. Choose `1` once to index the PDFs. Then choose `2` and ask questions.

## Important

If you used an older/broken version of this project, delete the old `chroma_db` folder before the first run. The application will recreate it.

Do not copy an old `.venv`, `chroma_db`, or `__pycache__` folder into this project.
