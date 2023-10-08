from .check_text import *
from .change_name import *
import docx
from doc2docx import convert
import antiword
import sys
import subprocess


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
        new_filepath = doc2docx(file_path)
        #os.remove(file_path)
        #file_path = file_path[:len(file_path) - 3] + 'docx'
        print(f'reading docx file from \'{new_filepath}\'')
        return read_docx(new_filepath)


def read_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    content = []
    for paragraph in doc.paragraphs:
        content.append(paragraph.text)
    return content


def doc2docx(filepath: str):
    new_filepath = filepath[:len(filepath) - 3] + 'docx'
    print(f'converting \'{filepath}\' to \'{new_filepath}\'')
    #tmp = convert(file_path, new_filepath)
    #tmp = 
    tmp = subprocess.run(['unoconv', '-d', 'document', '--format=docx', filepath])
    print(f'convert in doc2docx returned: {tmp}')
    return new_filepath


# print(read_file("backend/src/text-file-utility/test1.doc"))
