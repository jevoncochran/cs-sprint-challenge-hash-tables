def has_negatives(arr):
    collect_numbers = {}
    result = []

    for num in arr:
        # collect all nums to dict
        collect_numbers[num] = 1

        # if the number have correspinding negative numbers
        # add positive to array, no zeros
        if num != 0 and -num in collect_numbers:
            # push the absolute value to the result array
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))