import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    
    #2 array np
    x = np.array(x)
    p = np.array(p)

    #shape match
    if x.shape != p.shape:
        raise ValueError("Os arrays de valores (x) e probabilidades (p) devem ter o mesmo tamanho.")

    #tolerancia 10^-6
    if abs(np.sum(p) - 1.0) > 1e-6:
        raise ValueError("A soma das probabilidades deve ser igual a 1.")

    #multiplica valor pela probabilidade
    esperanca = np.sum(x * p)
    

    return float(esperanca)