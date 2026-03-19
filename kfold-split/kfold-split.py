import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    indices = np.arange(N, dtype=int)

    if shuffle:
        if rng is None:
            np.random.shuffle(indices)
        else:
            indices = rng.permutation(indices)


    base_size = N//k
    rem = N%k

    fold_sizes = np.full(k, base_size, dtype=int)
    fold_sizes[:rem] += 1

    folds = []
    start = 0
    for size in fold_sizes:
        end = start + size
        folds.append(indices[start:end])
        start += size

    results = []
    for i in range(k):
        validation = folds[i]
        training = np.concatenate([folds[j] for j in range(k) if j != i])
        results.append((training,validation))
    return results

    
    
