import numpy as np
import torch

from sklearn.metrics.pairwise import cosine_similarity
from src.text_vectorization import vectorize

def test_vectorize():
  inp1 = 'I love ASU'
  inp2 = 'i like asu'

  act1 = vectorize(inp1)
  act2 = vectorize(inp2)

  assert isinstance(act1, np.ndarray)
  assert len(act1.shape) == 2
  assert cosine_similarity(act1, act2) > 0.9
