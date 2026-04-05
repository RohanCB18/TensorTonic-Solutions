import numpy as np

def impute_missing(X, strategy='mean'):
    original_shape = np.array(X).shape
    X = np.array(X, dtype=float)
    X_imputed = X.copy()
    
    if X_imputed.ndim == 1:
        X_imputed = X_imputed.reshape(-1, 1)
    
    n_features = X_imputed.shape[1]
    
    for col in range(n_features):
        column_data = X_imputed[:, col]
        if np.any(np.isnan(column_data)):
            if np.all(np.isnan(column_data)):
                X_imputed[:, col] = 0
            else:
                if strategy == 'mean':
                    stat_value = np.nanmean(column_data)
                else:
                    stat_value = np.nanmedian(column_data)
                X_imputed[np.isnan(column_data), col] = stat_value
    
    return X_imputed.reshape(original_shape)