import argparse
import os

def list_documents(documents_dir="document"):
    """Lists PDF files in the specified documents directory.

    Args:
        documents_dir (str): The path to the documents directory.

    Returns:
        list: A list of PDF filenames found.
        int: Total count of PDF files.
        str: Message indicating if no PDF files were found.  
    """

    try:
        contents = os.listdir(documents_dir)
        pdf_files = [filename for filename in contents if filename.lower().endswith('.pdf')]

        if pdf_files:
            return pdf_files, len(pdf_files), ""  # Files found
        else:
            return [], 0, "No PDF files present."  # No files

    except FileNotFoundError:
        return [], 0, f"Error: Documents directory '{documents_dir}' not found."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List PDF documents in the 'documents' directory.")
    parser.add_argument("--dir", help="Specify an alternative documents directory.")
    args = parser.parse_args()

    documents_dir = "document" 
    if args.dir:
        documents_dir = args.dir

    filenames, count, message = list_documents(documents_dir)

    if count > 0:
        print("PDF files found:")
        for filename in filenames:
            print(filename)
        print(f"Total count: {count}")
    else:
        print(message) 
