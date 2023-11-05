import whisper
import os

model = whisper.load_model(
    'tiny', device='cpu')


def transcribe(filename: str) -> str:
    '''expects an audio filename, and transcribes it'''
    if not os.path.exists(filename):
        raise ValueError(f'\'{filename}\' does not exist')
    return model.transcribe(filename)['text'].strip()
