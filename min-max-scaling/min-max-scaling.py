def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    if not data or not data[0]:
        return []

    rows = len(data)
    cols = len(data[0])
    col_min = [float('inf')]*cols
    col_max = [float('-inf')]*cols

    for i in range(rows):
        for j in range(cols):
            col_min[j] = min(col_min[j],data[i][j])
            col_max[j] = max(col_max[j],data[i][j])

    result = []


    for i in range(rows):
        new_row = []
        for j in range(cols):
            max_val = col_max[j]
            min_val = col_min[j]
            range_val = max_val - min_val
            if range_val == 0:
                new_row.append(0.0)
            else:
                new_row.append((data[i][j] - min_val) / range_val)
        result.append(new_row)
    return result
            
            
    