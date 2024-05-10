import argparse
import PyPDF2  # type: ignore
import os

def retrieve(pdf_filename, documents_dir="document"):
    """Retrieves a PDF and returns its contents in a suitable format for chunking.

    Args:
        pdf_filename (str): The name of the PDF file to retrieve.
        documents_dir (str): The directory containing the PDF files.

    Returns:
        dict: A dictionary containing:
            * 'filename': The name of the PDF file.
            * 'content': The text content of the PDF.
    """

    filepath = os.path.join(documents_dir, pdf_filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"PDF file '{pdf_filename}' not found in '{documents_dir}'")

    with open(filepath, 'rb') as f:  # Reading in binary mode for PDF
        pdf_reader = PyPDF2.PdfReader(f)
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()

    return {'filename': pdf_filename, 'content': text_content} 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve a PDF for chunking.")
    parser.add_argument("--pdf_file", required=True, help="The name of the PDF file.")
    args = parser.parse_args()

    pdf_data = retrieve(args.pdf_file)
    print(pdf_data)  # This will print the filename and content