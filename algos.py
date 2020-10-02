class Algos:
    def __init__(self):
        pass
    
    def binary_search(arr: list, item) -> int:
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
        return -1
    
    
    def linear_search(arr: list, item) -> int:
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
        return -1
    
    def qsort(arr: list) -> list:
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
        
    def selection_sort(arr: list) -> list:
        """
        Returns a sorted array in O(n^2) time
        ----------
            arr : list, array
                the array to sort
        """
        for i in range(0, len(arr)-1):
            small = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[small]:
                    small = j
            temp_i = arr[i]
            arr[i] = arr[small]
            arr[small] = temp_i
        return arr