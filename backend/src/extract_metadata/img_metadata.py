from PIL import Image
from PIL.ExifTags import TAGS


def print_image_metadata(image_path):
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Extract EXIF data
            exif_data = img._getexif()

            metadata = {
                'author': "Unknown",
                'Create Date': "MM-DD-YYYY"
            }

            # If EXIF data is available
            if exif_data is not None:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)

                    if tag_name == 'Artist':
                        metadata['author'] = value

                    if tag_name == 'DateTimeOriginal':
                        metadata['Create Date'] = value

    except Exception as e:
        print(f"Error: {e}")


# print_image_metadata("backend/tests/scan0008.jpg")
