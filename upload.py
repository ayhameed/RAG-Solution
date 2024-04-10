import argparse
import os
import itertools

def upload(pdf_file):
    """Uploads a PDF file to the 'document' folder with an index in the filename.

    Args:
        pdf_file (str): Path to the PDF file to be uploaded.
    """

    upload_folder = "document"

    # Ensure the 'document' folder exists
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)  # Create the folder if needed

    index_file = os.path.join(upload_folder, "index.txt")  # Index stored in a file
    file_index = 1

    # Read existing index if available
    if os.path.exists(index_file):
        with open(index_file, 'r') as f:
            file_index = max(int(line.strip()) for line in f) + 1

    # Construct indexed filename 
    filename = os.path.basename(pdf_file)
    indexed_filename = f"file_{filename}"
    destination_path = os.path.join(upload_folder, indexed_filename)

    os.rename(pdf_file, destination_path)  # Move the file to the destination

    print("Upload successful!")
    print("Uploaded path and filename:", destination_path)

    # Update the index file
    with open(index_file, 'a') as f:
        f.write(f"{file_index}\n")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Upload a PDF file to the 'document' folder.")
    parser.add_argument("--pdf_file", required=True, help="Path to the PDF file you want to upload.")
    args = parser.parse_args()

    # Call the function to upload the PDF
    upload(args.pdf_file)
