"""
File: image_ocr.py
Project: SouL--DigitalRecordsManagementforMuseumsandHistoricalSites
File Created: 8th Oct 2023 4:18 am, Sunday
Author: Saurabh Zinjad (GitHub: Ztrimus)
Email: zinjadsaurabh1997@gmail.com

Copyright (c) 2023 Saurabh Zinjad
"""

# !pip install pytesseract
# !pip install pillow
# !pip install opencv-python

# # for linux
# !sudo apt update
# !sudo apt install tesseract-ocr
# !sudo apt install libtesseract-dev

from PIL import Image
import pytesseract
import numpy as np
import cv2
import os


def img_preprocessing(filename):
    image = cv2.imread(filename)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    resized_image = cv2.resize(
        enhanced, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC
    )
    return resized_image


def image_ocr(file):
    preprocessed_img = img_preprocessing(file)
    return pytesseract.image_to_string(preprocessed_img)
