# Text File Utility

This document explains how to use the provided Python files for working with text files of different formats (`txt`, `doc`, `docx`). The Python files include functions for checking if a file is a valid text file, reading text files, and converting `.doc` files to `.docx`.

## Prerequisites

Make sure you have the required dependencies installed before using the image captioning function. All of the dependencies can be found in `backend/src/requirements.txt`.

## Usage
First, import the txt-reader.py file, which contains the necessary functions for checking the files and read `txt`, `doc`, and `docx` files. Additionally, this script updates old `doc` files format into a more modern `docx` format.
- Import the Python files:
```Python
from txt-reader import *
```
- Use the `read_file` function:
```Python
result = read_file("backend/src/text-file-utility/test1.doc") // relative path from your working repo
```
- Output will be a Python list:
```Python
print(result)
// ["A beautiful view of the city skyline at night./n", "A beautiful view of the city skyline at night./n", "End"]
```