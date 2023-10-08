from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(input_file, output_file):
    # Load the video clip
    video_clip = VideoFileClip(input_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to an MP3 file
    audio_clip.write_audiofile(output_file)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()


"""
## Example usage
input_file_path = 'test.mp4'
output_file_path = 'out.mp3'

convert_mp4_to_mp3(input_file_path, output_file_path)
"""
