import argparse
import os

def delete(pdf_filename, documents_dir="document"):
    """Deletes a PDF file from the specified documents directory.

    Args:
        pdf_filename (str): The name of the PDF file to delete.
        documents_dir (str): The path to the documents directory.

    Returns:
        str: A message indicating success or failure.
    """

    filepath = os.path.join(documents_dir, pdf_filename)

    if not os.path.exists(filepath):
        return f"Error: PDF file '{pdf_filename}' not found in '{documents_dir}'."
    

    # Get PDF count before deletion
    pdf_count_before = len([name for name in os.listdir(documents_dir) if name.lower().endswith('.pdf')])

    try:
        os.remove(filepath)
        # Get PDF count after deletion
        pdf_count_after = len([name for name in os.listdir(documents_dir) if name.lower().endswith('.pdf')])

        print(f"PDF count before deletion: {pdf_count_before}")
        print(f"PDF count after deletion: {pdf_count_after}")
        return f"{pdf_filename} deleted successfully."

    except OSError as e:
        return f"Error deleting file: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete a PDF file from the 'documents' directory.")
    parser.add_argument("--pdf_file", required=True, help="The name of the PDF file to delete.") 
    parser.add_argument("--dir", help="Optional: Specify an alternative documents directory.")
    args = parser.parse_args()

    if args.dir:
        documents_dir = args.dir

    result = delete(args.pdf_file, documents_dir='document')
    print(result)
