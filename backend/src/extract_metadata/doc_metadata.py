from docx import Document
from helper import convert_docx_format


def view_docx_metadata(docx_path: str) -> dict:
    """
    View metadata information from a Microsoft Word (.docx) document.

    Parameters:
    - docx_path (str): The path to the Word document (.docx).

    Returns:
    - dict: A dictionary containing metadata information.
      Example:
      {
          'author': 'Unknown',
          'Create Date': None
      }

    Note:
    This function extracts metadata information, such as author and creation date,
    from the specified Word document. If the information is not available, default
    values are provided.

    Dependencies:
    - Requires the 'docx' library.
    - The 'convert_docx_format' function from the 'helper' module is used to format dates.

    Example:
    ```python
    metadata = view_docx_metadata("path/to/document.docx")
    print(metadata)
    ```

    :param docx_path: The path to the Word document (.docx).
    :type docx_path: str
    :return: A dictionary containing metadata information.
    :rtype: dict
    """
    doc = Document(docx_path)

    # Accessing core properties
    core_props = doc.core_properties
    metadata = {
        'author': 'Unknown',
        'Create Date': None
    }
    if core_props.author:
        metadata['author'] = core_props.author
    if core_props.created:
        metadata['Create Date'] = convert_docx_format(core_props.created)

    return metadata
