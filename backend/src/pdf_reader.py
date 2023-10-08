import os
from pypdf import PdfReader


def read_pdf(filename: str) -> str:
    if not os.path.exists(filename):
        raise ValueError(f'\'{filename}\' does not exist')
    reader = PdfReader(filename)
    all_text = ' '.join(
        [x.strip() for page in reader.pages for x in page.extract_text().strip().split('\n') if x])
    assert isinstance(all_text, str)
    return all_text
