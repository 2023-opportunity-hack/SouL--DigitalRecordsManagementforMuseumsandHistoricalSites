from .check_text import is_text_file
from .change_name import rename_file
import docx
from doc2docx import convert
import os


def read_text_file(file_path: str) -> str:
    """
    Read the content of a text file.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - str: The content of the text file.

    Example:
    ```python
    content = read_text_file("path/to/textfile.txt")
    print(content)
    ```

    :param file_path: The path to the file.
    :type file_path: str
    :return: The content of the text file.
    :rtype: str
    """
    if not is_text_file(file_path):
        return "Not a valid text file path."

    file_extension = file_path[-4:].lower()

    # Read the file based on its extension
    if file_extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as txt_file:
            return txt_file.read()

    elif file_extension == '.docx':
        return read_docx(file_path)

    elif file_extension == '.doc':
        doc2docx(file_path)
        os.remove(file_path)
        file_path = file_path[:-3] + 'docx'
        return read_docx(file_path)


def read_docx(file_path: str) -> str:
    """
    Read the content of a DOCX file.

    Parameters:
    - file_path (str): The path to the DOCX file.

    Returns:
    - str: The content of the DOCX file.

    :param file_path: The path to the DOCX file.
    :type file_path: str
    :return: The content of the DOCX file.
    :rtype: str
    """
    doc = docx.Document(file_path)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return '\n'.join(content)


def doc2docx(file_path: str):
    """
    Convert a DOC file to DOCX format.

    Parameters:
    - file_path (str): The path to the DOC file.

    :param file_path: The path to the DOC file.
    :type file_path: str
    """
    convert(file_path, file_path[:-3] + 'docx')

# Uncomment the following line to test the function
# content = read_text_file("backend/src/text-file-utility/test1.doc")
# print(content)
