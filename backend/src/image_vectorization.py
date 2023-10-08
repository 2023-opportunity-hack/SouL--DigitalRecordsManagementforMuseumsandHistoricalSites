import torch
import torchvision
import torchvision.transforms.functional as TF
import numpy as np
import os

from PIL import Image

# Disable gradient calculation since we are only doing inference
torch.set_grad_enabled(False)

# Specify the model name
MODEL_NAME = 'ResNet50_Weights.DEFAULT'

# Load the ResNet-50 model
print(f'Loading {MODEL_NAME} model')
img_model = torchvision.models.resnet50(weights=MODEL_NAME).eval()

# Define a class to save the output of a module during forward pass


class SaveOutput:
    def __init__(self):
        self.output = []

    def __call__(self, module, inp, out):
        self.output.append(out)

    def __getitem__(self, index):
        return self.output[index]

    def clear(self):
        self.output = []


# Instantiate SaveOutput and register the hook to the 'avgpool' submodule of the ResNet-50 model
save_out = SaveOutput()
hook_handle = img_model.get_submodule(
    'avgpool').register_forward_hook(save_out)


def vectorize(filename: str) -> np.ndarray:
    """
    Vectorize an image using a pre-trained ResNet-50 model.

    Parameters:
    - filename (str): The path to the image file.

    Returns:
    - np.ndarray: The vectorized representation of the image.

    Example:
    ```python
    filename = 'path/to/image.jpg'
    vec = vectorize(filename)
    print(vec)
    ```

    :param filename: The path to the image file.
    :type filename: str
    :return: The vectorized representation of the image.
    :rtype: np.ndarray
    """
    # Load the image
    if os.path.exists(filename):
        img = Image.open(filename)
    else:
        raise ValueError(f'{filename} does not exist')

    # Resize and convert the image to a torch tensor
    img = TF.resize(img, size=(224, 224))
    img = TF.to_tensor(img).unsqueeze(0)

    # Forward pass through the ResNet-50 model to get the vectors
    img_model(img)
    vec = save_out[0].squeeze()
    save_out.clear()

    # Convert the vectors to a numpy array and return
    return vec.numpy()
