from pptx2pdf.pptx_converter import pptx2text
from image_captioning_module.image_caption import caption
from text_file_utility.txt_reader import read_text_file
from video2audio.video_converter import convert_mp4_to_mp3
from pdf_reader import read_pdf
from speech_transcription import transcribe
from text_vectorization import vectorize
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')


def preprocess_input_to_str(file_path: str) -> str:
    audio_exts = ['.mp3']
    video_exts = ['.mp4']
    pdf_exts = ['.pdf']
    img_exts = ['.jpg', 'jpeg', '.png']
    text_exts = ['.doc', 'docx', '.txt']
    ppt_exts = ['pptx']

    file_ext = file_path[len(file_path)-4:]
    if (file_ext in audio_exts):
        return transcribe(file_path)
    elif (file_ext in video_exts):
        mp3_path = file_path[:len(file_path)-3] + 'mp3'
        convert_mp4_to_mp3(file_path, mp3_path)
        return transcribe(mp3_path)
    elif (file_ext in pdf_exts):
        return read_pdf(file_path)
    elif (file_ext in img_exts):
        return caption(file_path)
    elif (file_ext in text_exts):
        return read_text_file(file_path)
    elif (file_ext in ppt_exts):
        return pptx2text(file_path)


def preprocess(file_path: str) -> str:
    data = preprocess_input_to_str(file_path)
    tokenized_sentences = sent_tokenize(data, language='english')
    chunks = []
    for i in range(0, len(tokenized_sentences), 3):
        chunks.append(' '.join(tokenized_sentences[i:i+3]))

    vectors = [vectorize(vectorized_chunk) for vectorized_chunk in chunks]
    return vectors
