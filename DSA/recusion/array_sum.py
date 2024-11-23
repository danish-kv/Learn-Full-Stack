def rev_sum(arr, n):
    """
    Computes the sum of elements in an array using recursion.

    The function takes an array and the index of the last element (n) 
    as inputs, recursively computes the sum of the array elements 
    starting from the last element down to the first.

    Parameters:
    ----------
    arr : list
        A list of integers or floats to be summed.
    n : int
        The index of the current element to include in the sum 
        (usually initialized to len(arr) - 1 for the full array).

    Returns:
    -------
    int or float
        The sum of the elements in the array up to index n.

    Raises:
    ------
    IndexError
        If the input index n is out of bounds for the array.

    Example:
    --------
    >>> arr = [1, 2, 3, 4, 5]
    >>> rev_sum(arr, len(arr) - 1)
    15

    >>> arr = [10, 20, 30]
    >>> rev_sum(arr, len(arr) - 1)
    60
    """
    if n == 0:
        return arr[0]
    return arr[n] + rev_sum(arr, n - 1)
