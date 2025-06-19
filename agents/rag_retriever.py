# Refactored agents/rag_retriever.py
from langchain.agents import tool
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

openai_key = os.getenv("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")
if not openai_key:
    raise ValueError("Missing OPENAI_API_KEY. Please set it in your environment or Streamlit secrets.")

@tool
def retrieve_best_practices(query: str) -> str:
    """Retrieves accessibility best practices using RAG."""
    loader = TextLoader("agents/text.txt")
    docs = loader.load()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(openai_api_key=openai_key), retriever=vectorstore.as_retriever())
    return qa.run(query)
