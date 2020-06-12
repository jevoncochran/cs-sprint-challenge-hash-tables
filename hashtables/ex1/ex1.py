def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(length):
        current_weight = weights[i]
        # check if searched weight in cache, counterpart inserted previously
        if current_weight in cache:
            # get the index of previous weight
            previously_seen_index = cache[current_weight]

            return (i, previously_seen_index)

        # subtract and add to the key. Add index as a value
        cache[limit - weights[i]] = i

    return None



weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))


