from pypdf import PdfReader
from helper import convert_pdf_date


def view_pdf_metadata(pdf_path):
    """
    View metadata information from a PDF document.

    Parameters:
    - pdf_path (str): The path to the PDF document.

    Returns:
    - dict: A dictionary containing metadata information.
      Example:
      {
          'author': 'Unknown',
          'Create Date': None
      }

    Note:
    This function extracts metadata information, such as author and creation date,
    from the specified PDF document. If the information is not available, default
    values are provided.

    Dependencies:
    - Requires the 'pypdf' library.
    - The 'convert_pdf_date' function from the 'helper' module is used to format dates.

    Example:
    ```python
    metadata = view_pdf_metadata("path/to/document.pdf")
    print(metadata)
    ```

    :param pdf_path: The path to the PDF document.
    :type pdf_path: str
    :return: A dictionary containing metadata information.
    :rtype: dict
    """
    reader = PdfReader(pdf_path)

    # Accessing core properties
    core_props = reader.metadata
    metadata = {
        'author': 'Unknown',
        'Create Date': None
    }

    # Check if 'Creator' information is available
    if '/Creator' in core_props:
        metadata['author'] = core_props['/Creator']

    # Check if 'CreationDate' information is available
    if '/CreationDate' in core_props:
        try:
            # Attempt to convert and format the creation date
            metadata['Create Date'] = convert_pdf_date(
                core_props['/CreationDate'])
        except Exception as e:
            # Handle any errors that might occur during date conversion
            print(f"Error converting date: {e}")

    return metadata

# Uncomment the following line to test the function
# view_pdf_metadata("backend/tests/dummy.pdf")
