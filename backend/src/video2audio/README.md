# Video to Audio Converter with Moviepy

This Python script demonstrates how to convert an MP4 video file to an MP3 audio file using the [moviepy](https://zulko.github.io/moviepy/) library.

## Prerequisites

Make sure you have the required dependencies installed before using the image captioning function. All of the dependencies can be found in `backend/src/requirements.txt`.

## Usage
First, import the video-converter.py file, which contains the necessary functions for creating an audio file from the given video.
- Import the Python files:
```Python
from video-converter import *
```
- Use the `convert_mp4_to_mp3` function:
```Python
input_file_path = 'test.mp4' // relative path from your working repo
output_file_path = 'out.mp3' // relative path from your working repo

convert_mp4_to_mp3(input_file_path, output_file_path) 
```
- Output will be a audio file with the same name in the same directory but different file extension (from `mp4` to `mp3`).