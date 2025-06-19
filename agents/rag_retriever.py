# Refactored agents/rag_retriever.py
from langchain.agents import tool
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

@tool
def retrieve_best_practices(query: str) -> str:
    """Retrieves accessibility best practices using RAG."""
    loader = TextLoader("agents/text.txt")
    docs = loader.load()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=vectorstore.as_retriever())
    return qa.run(query)
