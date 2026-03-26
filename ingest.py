import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

def ingest_documents(pdf_folder="data"):
    docs = []
    
    files = os.listdir(pdf_folder)
    print(f"Files found in data/: {files}")
    
    for file in files:
        path = os.path.join(pdf_folder, file)
        
        if file.endswith(".pdf"):
            print(f"Loading PDF: {file}...")
            loader = PyPDFLoader(path)
            docs.extend(loader.load())
            
        elif file.endswith(".docx"):
            print(f"Loading Word doc: {file}...")
            loader = Docx2txtLoader(path)
            docs.extend(loader.load())
            
        else:
            print(f"Skipping unsupported file: {file}")
    
    if not docs:
        print("No supported files found.")
        return
    
    print(f"Splitting {len(docs)} pages into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    
    print(f"Embedding {len(chunks)} chunks and uploading to Pinecone...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    
    PineconeVectorStore.from_documents(
        chunks,
        embeddings,
        index_name="climateiq-zim",
        pinecone_api_key=os.getenv("PINECONE_API_KEY")
    )
    
    print(f"Done! {len(chunks)} chunks uploaded to Pinecone!")

if __name__ == "__main__":
    ingest_documents()
    
    