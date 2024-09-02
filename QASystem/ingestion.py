from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path
import os
from dotenv import load_dotenv

def pinecone_config():
    load_dotenv()
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = "default"

    document_store = PineconeDocumentStore(
        api_key=api_key,
        index=index_name,
        namespace="default",
        dimension=768
    )
    
    return document_store

def ingest(document_store):
    indexing = Pipeline()
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))

    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    indexing.run({"converter": {"sources": [Path("C:\\Users\\SanketPawarSP\\ml projects\\End to End RAG Application Using Haystack MistralAI Pinecone & FastAPI\\data\\Retrieval-Augmented-Generation-for-NLP.pdf")]}})
 
if __name__ == "__main__":
    document_store = pinecone_config()
    ingest(document_store)
