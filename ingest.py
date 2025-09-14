# ingest.py
from pathlib import Path
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def ingest_pdf(pdf_path: str, index_dir: str = "data/faiss_index", chunk_size: int = 1000, chunk_overlap: int = 200):
    """
    Load a PDF, split into chunks, embed with OpenAIEmbeddings, and build a FAISS vectorstore saved under index_dir.
    Returns the vectorstore instance.
    """
    Path(index_dir).mkdir(parents=True, exist_ok=True)

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    # persist to disk
    vectorstore.save_local(index_dir)

    return vectorstore

def load_vectorstore(index_dir: str = "data/faiss_index"):
    """
    Load a previously saved FAISS index from disk.
    """
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(index_dir, embeddings)
