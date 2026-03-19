import numpy as np

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    result = []
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    XtX = X.T@X

    d = XtX.shape[0]
    I = np.eye(d)

    reg = XtX + lam*I
    reg_inv = np.linalg.inv(reg)

    Xty = X.T @ y
    w = reg_inv @ Xty

    return w.tolist()
    
    