from transformers import AutoTokenizer, AutoModel
import numpy as np
import torch
torch.set_grad_enabled(False)


model_path = '/Users/rohan/3_Resources/ai_models/all-mpnet-base-v2'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)
model.eval()

# Following function is taken from huggingface's documentation on how to use the model
# Mean Pooling - Take attention mask into account for correct averaging


def mean_pooling(model_output, attention_mask):
    # First element of model_output contains all token embeddings
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(
        -1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def vectorize(text: str) -> np.ndarray:
    encoded_input = tokenizer(
        text, padding=True, truncation=True, return_tensors='pt')
    model_output = model(**encoded_input)
    return mean_pooling(model_output, encoded_input['attention_mask']).detach().numpy()
