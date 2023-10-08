from docx import Document
from helper import convert_docx_format


def view_docx_metadata(docx_path):
    doc = Document(docx_path)

    # Accessing core properties
    core_props = doc.core_properties
    metadata = {
        'author': 'Unknown',
        'Create Date': 'MM-DD-YYYY'
    }
    if (core_props.author):
        metadata['author'] = core_props.author
    if (core_props.created):
        metadata['Create Date'] = convert_docx_format(core_props.created)

    return metadata


# view_docx_metadata("backend/tests/test.docx")
