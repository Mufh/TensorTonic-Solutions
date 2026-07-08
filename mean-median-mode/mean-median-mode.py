import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x_arr = np.array(x)
    media = float(np.mean(x_arr))
    mediana = float(np.median(x_arr))
    
    contagem = Counter(x_arr)
    max_freq= max(contagem.values())

    candidatos_moda = [numero for numero, freq in contagem.items() if freq == max_freq]

    moda = float(min(candidatos_moda))

    return (media, mediana, moda)
    pass