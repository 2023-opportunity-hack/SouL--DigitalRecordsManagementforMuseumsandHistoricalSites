from .pptx2text.pptx_converter import pptx2text
from .image_captioning_module.image_caption import caption
from .text_file_utility.txt_reader import read_text_file
from .video2audio.video_converter import convert_mp4_to_mp3
from .pdf_reader import read_pdf
from .speech_transcription import transcribe
from .text_vectorization import vectorize
from database.elasticSearchClass import ES, ElasticSearchReqDoc
from .extract_metadata.control import get_metadata

from nltk.tokenize import sent_tokenize

audio_exts = ['m4a', 'wav', 'mp3']
video_exts = ['mp4']
pdf_exts = ['pdf']
img_exts = ['jpg', 'jpeg', 'png']
text_exts = ['doc', 'docx', 'txt']
ppt_exts = ['pptx']


def preprocess_input_to_str(file_path: str) -> str:
    """
    Preprocess different file types to text.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - str: The preprocessed text.

    Example:
    ```python
    preprocessed_text = preprocess_input_to_str("path/to/file.mp4")
    print(preprocessed_text)
    ```

    :param file_path: The path to the file.
    :type file_path: str
    :return: The preprocessed text.
    :rtype: str
    """
    file_ext = file_path.split('.')[-1]
    if file_ext in audio_exts:
        return transcribe(file_path)
    elif file_ext in video_exts:
        mp3_path = file_path[:-3] + 'mp3'
        convert_mp4_to_mp3(file_path, mp3_path)
        return transcribe(mp3_path)
    elif file_ext in pdf_exts:
        return read_pdf(file_path)
    elif file_ext in img_exts:
        return caption(file_path)
    elif file_ext in text_exts:
        return read_text_file(file_path)
    elif file_ext in ppt_exts:
        return pptx2text(file_path)


def preprocess(file_path: str):
    """
    Preprocess a file and store the result in ElasticSearch.

    Parameters:
    - file_path (str): The path to the file.

    Example:
    ```python
    preprocess("path/to/file.mp4")
    ```

    :param file_path: The path to the file.
    :type file_path: str
    """
    data = preprocess_input_to_str(file_path)

    if isinstance(data, list):
        data = ' '.join(x for x in data if x)
    elif not isinstance(data, str):
        print(type(data))

    # Tokenize the text into sentences
    tokenized_sentences = sent_tokenize(data, language='english')

    chunks = []
    # Chunk sentences into groups of 3
    for i in range(0, len(tokenized_sentences), 3):
        chunks.append(' '.join(tokenized_sentences[i:i+3]))

    # Store chunks in ElasticSearch
    fn = file_path.split('/')[-1]
    file_ext = file_path.split('.')[-1]

    for i, chunk in enumerate(chunks):
        doc = ElasticSearchReqDoc(
            filename=fn,
            chunk_id=i,
            file_type=file_ext,
            # You may want to dynamically retrieve the creation date
            creation_date=get_metadata(file_path)['Create Date'],
            feat_vec=vectorize(chunk).squeeze().tolist(),
        )
        ES.insert_document(doc)

    return None
