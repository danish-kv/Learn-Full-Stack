def linear_search(arr, target):
    """
    Performs a linear search to find the index of a target element in a list.

    The function iterates through the list and compares each element with 
    the target. If a match is found, it returns the index of the element. 
    If the target is not found, it returns `None`.

    Parameters:
    ----------
    arr : list
        A list of elements (can be integers, strings, etc.) where the search will be performed.
    target : any
        The element to search for in the list. It can be of any type that is comparable to the elements in the list.

    Returns:
    -------
    int or None
        The index of the target element if found; otherwise, `None` if the target is not in the list.

    Example:
    --------
    >>> linear_search([12, 2, 3, 4, 5, 5], 2)
    1

    >>> linear_search([1, 3, 5, 7, 9], 4)
    None
    """
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return None
