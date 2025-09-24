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

