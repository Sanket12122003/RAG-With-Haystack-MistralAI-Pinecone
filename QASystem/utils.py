from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['HF_API_TOKEN'] = HF_TOKEN
    
print("Import Successfully")

def pinecone_config():
    #configuring pinecone database
    document_store = PineconeDocumentStore(
            environment="gcp-starter",
            index="default",
            namespace="default",
            dimension=768
        )
    return document_store