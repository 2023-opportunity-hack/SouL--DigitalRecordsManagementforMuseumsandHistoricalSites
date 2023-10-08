# Image Captioning with Python

This document explains how to use the provided Python files for image captioning. The Python files include a function `caption` that takes a relative image file path as an argument and returns the generated caption for the image.

## Prerequisites

Make sure you have the required dependencies installed before using the image captioning function. All of the dependencies can be found in `backend/src/requirements.txt`.

## Usage
First, import the check_image.py file, which contains the necessary functions for checking if a file is a valid image.
- Import the Python files:
```Python
from image_caption import *
```
- Use the `caption` function:
```Python
result = caption("./backend/src/image-captioning-module/test.jpg") // relative path from your working repo
```
- Output will be a Python string:
```Python
print(result)
// A beautiful view of the city skyline at night.
```