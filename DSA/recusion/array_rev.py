def rev(arr, left, right):
    """
    Reverses the elements of an array in-place using recursion.

    The function recursively swaps the elements at the `left` and `right` indices 
    of the array and then moves inward towards the center of the array. 
    This process continues until the `left` index is greater than or equal to the `right` index.

    Parameters:
    ----------
    arr : list
        A list of elements (can be integers, strings, etc.) to be reversed.
    left : int
        The starting index (typically 0) to begin the reversal.
    right : int
        The ending index (typically len(arr) - 1) to begin the reversal.

    Returns:
    -------
    None
        The function modifies the input array in-place and does not return anything.

    Example:
    --------
    >>> arr = [1, 2, 3, 4, 5]
    >>> rev(arr, 0, len(arr) - 1)
    >>> print(arr)
    [5, 4, 3, 2, 1]

    >>> arr = ['a', 'b', 'c']
    >>> rev(arr, 0, len(arr) - 1)
    >>> print(arr)
    ['c', 'b', 'a']
    """
    if left >= right:
        return
    
    arr[left], arr[right] = arr[right], arr[left]

    return rev(arr, left + 1, right - 1)
