import numpy as np

import sys
print(sys.path)

from src.image_vectorization import vectorize

def test_vectorize():
  filename = './tests/scan0008.jpg'
  # Debug
  import os
  print(os.getcwd())
  # =====

  vec = vectorize(filename)
  assert isinstance(vec, np.ndarray)
  assert vec.shape == (2048, )
