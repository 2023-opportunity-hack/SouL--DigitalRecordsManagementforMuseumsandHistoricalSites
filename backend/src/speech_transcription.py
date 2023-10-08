import whisper
import os

# Load the Whisper ASR model
model = whisper.load_model(
    'tiny', device='cpu', download_root='/Users/rohan/3_Resources/ai_models/whisper')


def transcribe(filename: str) -> str:
    """
    Transcribe audio content using the Whisper ASR model.

    Parameters:
    - filename (str): The path to the audio file.

    Returns:
    - str: The transcribed text.

    Example:
    ```python
    transcribed_text = transcribe("path/to/audio.wav")
    print(transcribed_text)
    ```

    :param filename: The path to the audio file.
    :type filename: str
    :return: The transcribed text.
    :rtype: str
    """
    # Check if the file exists
    if not os.path.exists(filename):
        raise ValueError(f'\'{filename}\' does not exist')

    # Transcribe the audio using the Whisper ASR model
    transcribed_text = model.transcribe(filename)['text'].strip()

    return transcribed_text
