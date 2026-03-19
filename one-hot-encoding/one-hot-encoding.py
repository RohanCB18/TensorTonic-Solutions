import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y = np.asarray(y, dtype=int)
    if y.ndim != 1: 
        raise ValueError("y must be a 1D array")

    if num_classes is None:
        num_classes = np.max(y) + 1

    N = y.shape[0]

    one_hot_matrix = np.zeros((N,num_classes),dtype=float)

    for i in range(N):
        one_hot_matrix[i][y[i]] = 1

    return one_hot_matrix
    
    