from transformers import AutoTokenizer, AutoModel
import numpy as np
import torch

# Disable gradient calculation since we are only doing inference
torch.set_grad_enabled(False)

# Specify the path to the model
model_path = '/Users/rohan/3_Resources/ai_models/all-mpnet-base-v2'

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)
model.eval()

# Function to perform mean pooling on model output


def mean_pooling(model_output, attention_mask):
    """
    Perform mean pooling on the model output while taking attention mask into account.

    Parameters:
    - model_output (torch.Tensor): Model output containing token embeddings.
    - attention_mask (torch.Tensor): Attention mask indicating valid tokens.

    Returns:
    - torch.Tensor: Mean-pooled vector representation of the input text.

    :param model_output: Model output containing token embeddings.
    :type model_output: torch.Tensor
    :param attention_mask: Attention mask indicating valid tokens.
    :type attention_mask: torch.Tensor
    :return: Mean-pooled vector representation of the input text.
    :rtype: torch.Tensor
    """
    # Extract token embeddings from the model output
    token_embeddings = model_output[0]

    # Expand the attention mask to match the dimensions of token embeddings
    input_mask_expanded = attention_mask.unsqueeze(
        -1).expand(token_embeddings.size()).float()

    # Perform mean pooling while considering the attention mask
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def vectorize(text: str) -> np.ndarray:
    """
    Vectorize text using the specified model.

    Parameters:
    - text (str): The input text to be vectorized.

    Returns:
    - np.ndarray: The vector representation of the input text.

    Example:
    ```python
    text_vector = vectorize("This is an example sentence.")
    print(text_vector)
    ```

    :param text: The input text to be vectorized.
    :type text: str
    :return: The vector representation of the input text.
    :rtype: np.ndarray
    """
    # Tokenize and encode the input text
    encoded_input = tokenizer(
        text, padding=True, truncation=True, return_tensors='pt')

    # Get the model output
    model_output = model(**encoded_input)

    # Perform mean pooling to obtain the vector representation
    text_vector = mean_pooling(
        model_output, encoded_input['attention_mask']).detach().numpy()

    return text_vector
