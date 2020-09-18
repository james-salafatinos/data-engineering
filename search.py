def binary_search(arr, item):
    """
    Returns the index of the item if found, otherwise None. Time-complexity = O(log n)
    Parameters
    ----------
        arr : list, array
            the array to look in
        item : int, float
            the item to find
    """
    high_idx = len(arr)-1
    low_idx = 0

    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx)//2
        guess = arr[mid_idx]
        if guess == item:
            return mid_idx
        if guess < item:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    return None


def linear_search(arr, item):
    """
    Returns the index of item in array if found, otherwise None. Time-complexity = O(n)
    Parameters
    ----------
        arr : list, array
            the array to look in
        item : int, float
            the item to find
    """
    for i,potential in enumerate(arr):
        if item == potential:
            return i
        else:
            continue
    return None