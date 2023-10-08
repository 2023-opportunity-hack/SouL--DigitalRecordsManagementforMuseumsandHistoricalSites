# Assuming check_image.py has the is_image_file function
from .check_image import is_image_file
from transformers import AutoTokenizer, AutoModel
from transformers import pipeline

# Path to the pre-trained image-to-text model
model_path = '/Users/rohan/3_Resources/ai_models/vit-gpt2-image-captioning'

# Initialize the image-to-text pipeline
image_to_text = pipeline("image-to-text", model=model_path)


def caption(filename: str) -> str:
    """
    Generate a caption for an image using a pre-trained image-to-text model.

    Parameters:
    - filename (str): The path to the image file.

    Returns:
    - str: The generated caption for the image.

    Example:
    ```python
    caption_result = caption("path/to/image.jpg")
    print(caption_result)
    ```

    :param filename: The path to the image file.
    :type filename: str
    :return: The generated caption for the image.
    :rtype: str
    """
    # Uncomment the line below if you want to use a relative path
    # filename = os.path.join("../../", filename)

    # Check if the file is a valid image
    if not is_image_file(filename):
        return "Not a valid path. Image file may have been broken."

    # Generate a caption for the image using the pre-trained model
    result = image_to_text(filename)[0]['generated_text']

    return result

# Uncomment the following line to test the function
# print(caption("./backend/src/image_captioning_module/test.jpg"))
