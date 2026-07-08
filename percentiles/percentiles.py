import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x_sorted = np.sort(np.array(x))
    q = np.array(q)

    resultado = np.percentile(x_sorted, q, method='linear')

    return resultado
    
    pass