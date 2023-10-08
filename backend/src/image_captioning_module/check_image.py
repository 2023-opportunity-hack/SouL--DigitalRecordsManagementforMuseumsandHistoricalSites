import imghdr
import os


def is_image_file(file_path):
    """
    Check if a file is a valid image file based on its extension.

    Parameters:
    - file_path (str): The path to the file.

    Returns:
    - bool: True if the file is a valid image file, False otherwise.

    Example:
    ```python
    is_image = is_image_file("path/to/image.jpg")
    print(is_image)
    ```

    :param file_path: The path to the file.
    :type file_path: str
    :return: True if the file is a valid image file, False otherwise.
    :rtype: bool
    """
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

    return image_type is not None and image_type in valid_extensions
