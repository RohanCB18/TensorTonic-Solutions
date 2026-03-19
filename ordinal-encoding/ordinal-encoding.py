def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    mappings = {val : i for i,val in enumerate(ordering)}
    return [mappings[v] for v in values]