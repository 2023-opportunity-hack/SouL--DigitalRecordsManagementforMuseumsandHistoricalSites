from PIL import Image
from PIL.ExifTags import TAGS


def view_image_metadata(image_path):
    """
    Print image metadata, including author and creation date if available.

    Parameters:
    - image_path (str): The path to the image file.

    Example:
    ```python
    print_image_metadata("path/to/image.jpg")
    ```

    :param image_path: The path to the image file.
    :type image_path: str
    """
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Extract EXIF data
            exif_data = img._getexif()

            # Initialize metadata with default values
            metadata = {
                'author': "Unknown",
                'Create Date': None
            }

            # If EXIF data is available
            if exif_data is not None:
                # Iterate through EXIF tags and extract relevant information
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)

                    # Extract author information from the 'Artist' tag
                    if tag_name == 'Artist':
                        metadata['author'] = value

                    # Extract creation date information from the 'DateTimeOriginal' tag
                    if tag_name == 'DateTimeOriginal':
                        metadata['Create Date'] = value

    except Exception as e:
        # Handle any errors that might occur during processing
        print(f"Error: {e}")

# Uncomment the following line to test the function
# print_image_metadata("backend/tests/scan0008.jpg")
