from pptx import Presentation
from helper import convert_docx_format


def view_ppt_metadata(ppt_path):
    ppt = Presentation(ppt_path)

    # Accessing core properties
    core_props = ppt.core_properties
    metadata = {
        'author': 'Unknown',
        'Create Date': 'MM-DD-YYYY'
    }
    if (core_props.author):
        metadata['author'] = core_props.author
    if (core_props.created):
        metadata['Create Date'] = convert_docx_format(core_props.created)

    return metadata
