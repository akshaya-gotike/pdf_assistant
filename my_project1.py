import fitz  # PyMuPDF to handle PDF operations
import os

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    """
    Extracts text from the given PDF file.
    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF document.
    """
    doc = fitz.open(pdf_path)  # Open the PDF file using PyMuPDF
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text("text")  # Extract text from the page
    return text

# Function to perform keyword search
def keyword_search(text, keyword):
    """
    Searches for a keyword in the extracted text.
    Args:
        text (str): The extracted text from the PDF document.
        keyword (str): The keyword to search for in the text.
    Returns:
        str: The sentences containing the keyword or a message if not found.
    """
    keyword = keyword.lower()
    sentences = text.split('.')  # Split the text into sentences
    relevant_sentences = [sentence.strip() for sentence in sentences if keyword in sentence.lower()]
    
    if relevant_sentences:
        return "\n".join(relevant_sentences)
    else:
        return f"The keyword '{keyword}' was not found in the document."

# Function to generate a basic summary (first few sentences)
def generate_summary(text, num_sentences=5):
    """
    Generates a basic summary by extracting the first few sentences.
    Args:
        text (str): The extracted text from the PDF document.
        num_sentences (int): Number of sentences to include in the summary.
    Returns:
        str: The summary text.
    """
    sentences = text.split('.')
    summary = ' '.join(sentences[:num_sentences]).strip()
    return summary + ('.' if not summary.endswith('.') else '')

# Main script
def main():
    # Get the PDF file path from the user
    pdf_path = input("Enter the path to your PDF file: ").strip()

    # Check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"The file at {pdf_path} does not exist. Please check the path.")
        return

    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)

    # Get the keyword from the user
    keyword = input("Enter the keyword you want to search for: ").strip()

    # Perform keyword search
    search_result = keyword_search(text, keyword)
    print(f"\nKeyword search result:\n{search_result}\n")
# Run the script
if __name__ == "__main__":
    main()
