import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x_array = np.array(x, dtype=float)
    return 1 / (1 + np.exp(-x_array))
    pass