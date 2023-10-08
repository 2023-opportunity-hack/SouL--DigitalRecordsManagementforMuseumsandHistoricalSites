from pypdf import PdfReader
from helper import convert_pdf_date


def view_pdf_metadata(pdf_path):
    reader = PdfReader(pdf_path)

    # Accessing core properties
    core_props = reader.metadata
    metadata = {
        'author': 'Unknown',
        'Create Date': 'MM-DD-YYYY'
    }
    if (core_props['/Creator']):
        metadata['/Creator'] = core_props.author
    if (core_props['/CreationDate']):
        try:
            metadata['Create Date'] = convert_pdf_date(
                core_props['/CreationDate'])
        except:
            pass

    return metadata


# view_pdf_metadata("backend/tests/dummy.pdf")
