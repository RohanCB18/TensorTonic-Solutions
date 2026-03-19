import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X,dtype=float)
    X_min = np.min(X,axis=axis,keepdims=True)
    X_max = np.max(X,axis=axis,keepdims=True)

    X_range = X_max-X_min
    X_range_safe = np.where(X_range == 0, 1, X_range)
    X_scaled = (X-X_min)/X_range_safe
    X_scaled = np.where(X_scaled == 0,0.0,X_scaled)

    return X_scaled

    