def rev(words):
    """
    Recursively reverses a given string.

    The function takes a string as input and returns the reversed version 
    by extracting the last character of the string and appending it to the 
    result of a recursive call on the remaining substring.

    Parameters:
    ----------
    words : str
        The input string to be reversed.

    Returns:
    -------
    str
        The reversed string.

    Example:
    --------
    >>> rev("My Name is Danish")
    'hsinaD si emaN yM'

    >>> rev("hello")
    'olleh'

    >>> rev("")
    ''
    """
    if len(words) <= 1:
        return words
    return words[-1] + rev(words[:-1])
