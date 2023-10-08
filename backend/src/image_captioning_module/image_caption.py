from .check_image import *

from transformers import AutoTokenizer, AutoModel
from transformers import pipeline

model_path = '/Users/rohan/3_Resources/ai_models/vit-gpt2-image-captioning'
image_to_text = pipeline("image-to-text", model=model_path)

def caption(filename: str) -> str:
    # filename = os.path.join("../../", filename)
    if (not is_image_file(filename)):
        return "Not a valid path"

    result = image_to_text(filename)[0]['generated_text']

    return result


# print(caption("./backend/src/image-captioning-module/test.jpg"))
