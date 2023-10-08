from pptx2pdf.pptx_converter import pptx2text
from image_captioning_module.image_caption import caption
from text_file_utility.txt_reader import read_file
import sys


def preprocess_input(file_path):
    print(caption(file_path))
