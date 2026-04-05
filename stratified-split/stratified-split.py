import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    X = np.array(X)
    y = np.array(y)

    if rng is None:
        rng = np.random.default_rng(seed=42)

    unique_classes, class_counts = np.unique(y, return_counts=True)
    
    train_indices = []
    test_indices = []
    
    for cls in unique_classes:
        cls_indices = np.where(y == cls)[0]
        cls_count = len(cls_indices)
        n_test = int(round(cls_count * test_size))
        
        if n_test == 0 and cls_count > 0:
            n_test = 1
        if n_test == cls_count and cls_count > 1:
            n_test = cls_count - 1
        
        shuffled_indices = rng.permutation(cls_indices)
        test_indices.extend(sorted(shuffled_indices[:n_test]))
        train_indices.extend(sorted(shuffled_indices[n_test:]))
    
    train_indices = np.array(sorted(train_indices))
    test_indices = np.array(sorted(test_indices))
    
    if X.ndim == 1:
        X_train = X[train_indices]
        X_test = X[test_indices]
    else:
        X_train = X[train_indices, :]
        X_test = X[test_indices, :]
    
    y_train = y[train_indices]
    y_test = y[test_indices]
    
    return (X_train, X_test, y_train, y_test)