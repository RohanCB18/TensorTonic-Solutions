def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    n = len(values)
    if n == 1:
        return [0.0]

    arr = sorted(values)

    def median_finder(a):
        m = len(a)
        mid = m//2
        if m % 2 == 0:
            return (a[mid-1]+a[mid])/2
        else:
            return a[mid]

    median = median_finder(arr)

    mid = n//2
    if n % 2 == 0:
        lower = arr[:mid]
        upper = arr[mid:]
    else:
        lower = arr[:mid]
        upper = arr[mid+1:]

    Q1 = median_finder(lower)
    Q3 = median_finder(upper)
    IQR = Q3-Q1

    result = []
    for x in values:
        if IQR == 0:
            result.append(float(x-median))
        else:
            result.append((float(x-median))/IQR)
    return result
    
        
    
    