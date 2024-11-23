def factorial(n):
    """
    Computes the factorial of a given non-negative integer using recursion.

    The factorial of a number n (denoted as n!) is the product of all positive 
    integers from 1 to n. By definition, the factorial of 0 is 1.

    Parameters:
    ----------
    n : int
        The non-negative integer for which the factorial is to be computed.

    Returns:
    -------
    int
        The factorial of the input number n.

    Raises:
    ------
    ValueError
        If n is a negative integer.

    Example:
    --------
    >>> factorial(5)
    120

    >>> factorial(0)
    1
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
