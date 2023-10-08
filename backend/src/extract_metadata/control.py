from audio_metadata import *
from doc_metadata import *
from img_metadata import *
from pdf_metadata import *
from ppt_metadata import *
from video_metadata import *

audio_exts = ['m4a', 'wav', 'mp3']
video_exts = ['mp4']
pdf_exts = ['pdf']
img_exts = ['jpg', 'jpeg', 'png']
text_exts = ['doc', 'docx', 'txt']
ppt_exts = ['pptx']


def get_metadata(file_path):
    file_ext = file_path.split('.')[-1]
    if file_ext in audio_exts:
        return view_audio_metadata(file_path)
    elif file_ext in video_exts:
        return view_video_metadata(file_ext)
    elif file_ext in pdf_exts:
        return view_pdf_metadata(file_path)
    elif file_ext in img_exts:
        return view_image_metadata(file_path)
    elif file_ext in text_exts:
        return view_docx_metadata(file_path)
    elif file_ext in ppt_exts:
        return view_ppt_metadata(file_path)
