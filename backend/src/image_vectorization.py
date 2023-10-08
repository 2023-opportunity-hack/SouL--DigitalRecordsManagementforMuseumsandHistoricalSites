#!python3

import torch
import torchvision
import torchvision.transforms.functional as TF
import numpy as np
import os

from PIL import Image

torch.set_grad_enabled(False)
MODEL_NAME = 'ResNet50_Weights.DEFAULT'
print(f'loading {MODEL_NAME} model')
img_model = torchvision.models.resnet50(weights=MODEL_NAME).eval()

class SaveOutput:
  def __init__(self): self.output = []
  def __call__(self, module, inp, out): self.output.append(out)
  def __getitem__(self, index): return self.output[index]
  def clear(self): self.output = []

save_out = SaveOutput()
hook_handle = img_model.get_submodule('avgpool').register_forward_hook(save_out)

def vectorize(filename: str) -> np.ndarray:
  # load image
  if os.path.exists(filename): img = Image.open(filename)
  else: raise ValueError(f'{filename} does not exist')
  #if img.mode != 'RGB': img = 
  # convert to torch tensor
  img = TF.resize(img, size=(224, 224))
  img = TF.to_tensor(img).unsqueeze(0)
  # get vectors from hook
  img_model(img)
  vec = save_out[0].squeeze()
  save_out.clear()
  # convert to numpy array & return
  return vec.numpy()

