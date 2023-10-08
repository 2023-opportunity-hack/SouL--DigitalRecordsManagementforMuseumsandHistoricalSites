from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(input_file: str, output_file: str):
    """
    Convert a video file (MP4) to an audio file (MP3).

    Parameters:
    - input_file (str): The path to the input MP4 file.
    - output_file (str): The desired path for the output MP3 file.

    Example:
    ```python
    input_file_path = 'path/to/input_video.mp4'
    output_file_path = 'path/to/output_audio.mp3'
    convert_mp4_to_mp3(input_file_path, output_file_path)
    ```

    :param input_file: The path to the input MP4 file.
    :type input_file: str
    :param output_file: The desired path for the output MP3 file.
    :type output_file: str
    """
    # Load the video clip
    video_clip = VideoFileClip(input_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to an MP3 file
    audio_clip.write_audiofile(output_file)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

# Example usage:
# input_file_path = 'test.mp4'
# output_file_path = 'out.mp3'
# convert_mp4_to_mp3(input_file_path, output_file_path)
