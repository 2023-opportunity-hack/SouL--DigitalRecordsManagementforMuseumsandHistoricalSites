import os
from pypdf import PdfReader


def read_pdf(filename: str) -> str:
    """
    Read text content from a PDF file.

    Parameters:
    - filename (str): The path to the PDF file.

    Returns:
    - str: The extracted text content.

    Example:
    ```python
    text_content = read_pdf("path/to/document.pdf")
    print(text_content)
    ```

    :param filename: The path to the PDF file.
    :type filename: str
    :return: The extracted text content.
    :rtype: str
    """
    # Check if the file exists
    if not os.path.exists(filename):
        raise ValueError(f'\'{filename}\' does not exist')

    # Use PdfReader to read the PDF file
    reader = PdfReader(filename)

    # Extract text content from all pages, cleaning up formatting
    all_text = ' '.join(
        [x.strip() for page in reader.pages for x in page.extract_text(
        ).strip().split('\n') if x]
    )

    # Ensure the result is a string
    assert isinstance(all_text, str)

    return all_text
