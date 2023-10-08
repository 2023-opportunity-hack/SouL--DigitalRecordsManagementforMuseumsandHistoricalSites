from check_image import *


def caption(filename: str) -> str:
    # filename = os.path.join("../../", filename)
    if (not is_image_file(filename)):
        return "Not a valid path. Image file may have been broken."

    from transformers import AutoTokenizer, AutoModel
    from transformers import pipeline
    image_to_text = pipeline(
        "image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    result = image_to_text(filename)[0]['generated_text']

    return result


# print(caption("./backend/src/image_captioning_module/test.jpg"))
