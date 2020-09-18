def qsort(arr):
    """
    Returns a sorted array. Time-complexity = O(n log n)
    Parameters
    ----------
        arr : list, array
            the array to sort
    """
    #Base case  (already sorted)
    if len(arr) < 2:
        return arr
    #Recursive case
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return qsort(less) + [pivot] + qsort(greater)