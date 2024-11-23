def fibonacci(n):
    """
    Computes the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
    ----------
    n : int
        The position of the Fibonacci sequence to compute (0-indexed).

    Returns:
    -------
    int
        The nth Fibonacci number.

    Raises:
    ------
    ValueError
        If the input n is negative.

    Example:
    --------
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(10)
    55
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
