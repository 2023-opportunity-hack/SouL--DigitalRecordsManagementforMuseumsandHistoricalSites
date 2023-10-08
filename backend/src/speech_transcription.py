import whisper
import os

model = whisper.load_model(
    'tiny', device='cpu', download_root='/Users/rohan/3_Resources/ai_models/whisper')


def transcribe(filename: str) -> str:
    '''expects an audio filename, and transcribes it'''
    if not os.path.exists(filename):
        raise ValueError(f'\'{filename}\' does not exist')
    return model.transcribe(filename)['text'].strip()
