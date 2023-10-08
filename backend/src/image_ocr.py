import os

from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

model_path = '/Users/rohan/3_Resources/ai_models/trocr-base-handwritten'
processor = TrOCRProcessor.from_pretrained(model_path)
model = VisionEncoderDecoderModel.from_pretrained(model_path)

def extract_text(filename: str) -> str:
  if not os.path.exists(filename): raise ValueError(f'\'{filename}\' does not exist')
  img = Image.open(filename).convert('RGB')
  pixel_values = processor(img, return_tensors='pt').pixel_values
  gen_ids = model.generate(pixel_values)
  gen_text = processor.batch_decode(gen_ids, skip_special_tokens=True)[0]
  return gen_text

if __name__ == '__main__':
  print(extract_text('./sfs/ray-so-export.png'))
