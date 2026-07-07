import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    # Write code here  
    linhas, colunas = A.shape
    matriz_transposta = np.zeros((colunas, linhas))

    for i  in range(linhas):
        for j in range(colunas):
            matriz_transposta[j, i] = A[i, j]

    
    return matriz_transposta
    pass
