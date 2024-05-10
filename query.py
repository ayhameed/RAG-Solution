import os
import argparse
import warnings
import langchain  # type: ignore
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter  # type: ignore
from langchain_community.document_loaders import PyPDFLoader  # type: ignore
from dotenv import load_dotenv  # type: ignore
from langchain_community.vectorstores import FAISS  # type: ignore
from langchain_openai import OpenAIEmbeddings  # type: ignore
from langchain_community.document_loaders import TextLoader  # type: ignore
from langchain_openai import OpenAIEmbeddings  # type: ignore
from langchain_text_splitters import CharacterTextSplitter  # type: ignore
from langchain_community.vectorstores import FAISS  # type: ignore

def query(question):
    """
    Takes in a question and returns an answer.

    Args:
        question (str): Question to be asked.
    """
    load_dotenv()

    OPENAI_API_KEY = os.environ.get('Open_AI_API_Key')
    LANGCHAIN_API_KEY = os.environ.get('Lang_chain_API_Key')

    path_to_pdf = "document/file_proposal.pdf"  # Replace with your actual PDF path

    # Load the document, split it into chunks, embed each chunk and load it into the vector store.
    raw_documents = PyPDFLoader(path_to_pdf).load()

    # Mute errors
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # Split by chunks
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        documents = text_splitter.split_documents(raw_documents)
        
        db = FAISS.from_documents(documents, OpenAIEmbeddings())

        docs = db.similarity_search(question, k=1)

        for doc in docs:
            code_splitter = RecursiveCharacterTextSplitter()
            python_docs = code_splitter.split_text(doc.page_content)

            for code_chunk in python_docs:
                print(str(doc.metadata["page"]) + ":", code_chunk)
                print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ask a question.")
    parser.add_argument("--question", required=True, help="ask question")
    args = parser.parse_args()

    query(args.question)
