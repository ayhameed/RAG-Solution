# Project RAG (Spring 2024)

Retrieval-Augmented Generation for Question-Answering on PDFs

## Overview
This project levrages Langchain for piepline, weaviate for vectorDB and Stream it for UI.


## Dependencies 
- Python 3
- python-dotenv
- PyPDF2 
- pypdf 
- Faiss CPU
- Lang-chain
- LaNG-Chain OPENAI
- Weaviate
- StreamIt

## How to install
- Install the entire dependencies
     ```
        %pip install -r requirements.txt
    ```
## Or install the packages you need 
- PyPDF2
    ```
        %pip install pypdf
    ```
- pypdf 
    ```
        %pip install pypdf
    ```
- Python dot-env
    ```
        %pip install python-dotenv
    ```
- Faiss CPU
    ```
        pip install faiss-cpu  
    ```
- Langchain 
    ```
        %pip install langchain
    ```
- Langchain-openAI
    ```
        %pip install langchain-openai
    ```

## Functions 
- PDF Upload and Indexing
- PDF deletion
- Vector-Based Retrieval
- Question Answering

## Set up env
1. create a .env file
2. add the fields:
    -  OPENAI_API_KEY = 'your_api_key'
    -  LANG_CHAIN_API_KEY = 'your_api_key'
3. add the .env file to your gitignore 

## Usage Examples

### !Run all commands from cli with python integrated

## A. PDF Operations
1. `list.py`: Returns a list of all Uplaoded PDF's
   `Usage`: `python3 list.py`
    `Response`:
        `on success` : `Returns a list of pdf files and the count`
        `!successsful` : `Error: No PDF files present.`

2. `upload.py`: Uploads a pdf to a document directory
   `Usage`: `python3 upload.py --pdf_file=sample.pdf`
    `Response`:
        `on success` : 
            ```
            Upload successful! 
            Uploaded path and filename: document/file_sample.pdf
            ```
        `!successsful` : `[Errno 2] No such file or directory`

3. `retrieve.py`: Retrieves a pdf by name along with its content
   `Usage`: `python3 retrieve.py --pdf_file=sample.pdf`
    `Response`:
        `on success` : `{'filename': 'sample.pdf', 'content': "lifelong"}`
        `!successsful` : `Error: PDF file 'sample.pdf' not found in 'document'`

4. `delete.py`: Deletes a pdf by name and returns the current dir count
   `Usage`: `python3 delete.py --pdf_file=sample.pdf`
    `Response`:
        `on success` : `{'filename': 'sample.pdf', 'content': "lifelong"}`
        `!successsful` : 
            ```
            PDF count before deletion: 2
            PDF count after deletion: 1
            sample.pdf deleted successfully.
            ```

5. `query.py`: Queries  a pdf and returns an answer with a character limit of 300
   `Usage`: `python3 query.py --question="What are heat exchangers?"
    `Response`:
        `on success` : `{'page_number': 'answer'}`
        `!successsful` : 
            ```
                An error has occured 
            ```