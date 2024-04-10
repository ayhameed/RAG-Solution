import os
import argparse
import langchain
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def query(question):
    """
    Takes in a question and returns an answer.

    Args:
        question (str): Question to be asked.
    """
    load_dotenv()  

    OPENAI_API_KEY = os.environ.get('Open_AI_API_Key') 
    LANGCHAIN_API_KEY = os.environ.get('Lang_chain_API_Key')
    
    path_to_pdf = "document/file_proposal.pdf" # Replace with your actual PDF path
    
    loader = PyPDFLoader(path_to_pdf)
    pages = loader.load_and_split()
    
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
    
    docs = faiss_index.similarity_search(question, k=2)  # Update question here 
    
    for doc in docs:
        code_splitter = RecursiveCharacterTextSplitter()
        python_docs = code_splitter.split_text(doc.page_content)

        for code_chunk in python_docs:
            print(str(doc.metadata["page"]) + ":", code_chunk) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ask a question.")
    parser.add_argument("--question", required=True, help="ask question")
    args = parser.parse_args()

    query(args.question)
