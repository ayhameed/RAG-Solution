# Project RAG (Spring 2024)

Retrieval-Augmented Generation for Question-Answering on PDFs

## Overview
This project levrages Langchain for piepline, weaviate for vectorDB and Stream it for UI.

## Dependencies 
- Python 3
- PyPDF2 
- Langchain
- Weaviate
- StreamIt

## Functions 
- PDF Upload and Indexing
- PDF deletion
- Vector-Based Retrieval
- Question Answering

## Usage Examples

### ! run all commands from cli with python integrated

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
            Uploaded path and filename: document/file_1_sample.pdf
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
## B. Pipe Line Operations