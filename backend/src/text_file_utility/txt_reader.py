from check_text import *
from change_name import *
import docx
from doc2docx import convert


def read_text_file(file_path: str) -> str:
    if (not is_image_file(file_path)):
        return "Not a valid text file path."
    file_extension = file_path[len(file_path)-4:]

    # Read the file based on its extension
    if file_extension.lower() == '.txt':
        with open(file_path, 'r', encoding='utf-8') as txt_file:
            return txt_file.readlines()

    elif file_extension.lower() == 'docx':
        return read_docx(file_path)

    elif file_extension.lower() == '.doc':
        doc2docx(file_path)
        os.remove(file_path)
        file_path = file_path[:len(file_path) - 3] + 'docx'
        return read_docx(file_path)


def read_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return content


def doc2docx(file_path: str):
    convert(file_path, file_path[:len(file_path) - 3] + 'docx')


# print(read_file("backend/src/text-file-utility/test1.doc"))
