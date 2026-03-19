def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    result = {}
    for c,t in zip(categories, targets):
        if c not in result:
            result[c] = []
        result[c].append(t)

    mapping = {}
    for c,t in result.items():
        mapping[c] = sum(t)/len(t)

    answer = []
    for x in range(len(categories)):
        word = categories[x]
        answer.append(mapping[word])

    return answer
    