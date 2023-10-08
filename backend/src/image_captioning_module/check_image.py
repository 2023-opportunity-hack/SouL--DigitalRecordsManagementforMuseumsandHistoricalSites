import imghdr
import os

# TODO (rohan): merge all audio extensions into one

def is_image_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return False

    # Check if the file is a regular file
    if not os.path.isfile(file_path):
        return False

    # Check if the file extension corresponds to a valid image format
    image_type = imghdr.what(file_path)
    valid_extensions = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff',
                        'rast', 'xbm', 'jpeg', 'bmp', 'png', 'webp', 'exr', 'jpg']

    print(f'image type is: {image_type}')
    return image_type is not None and image_type.lower() in valid_extensions
