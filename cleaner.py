def filter_nondigits(data: list) -> list:
    """Filters out non-numeric strings from the input list and returns a list of integers.

    Args:
        data (list[int]): list of strings, where some may contain non-numeric characters.

    Returns:
        list: list containing only the numeric values from the input, converted to integers.
        
    Usage examples:
        >>> filter_nondigits(["10", "20", "30"])
        [10, 20, 30]

        >>> filter_nondigits(["  5 ", "\\n8", "12\\n"])
        [5, 8, 12]

        >>> filter_nondigits(["B00B", "123", "\\n", "456"])
        [123, 456]

        >>> filter_nondigits(["   ", "\\n"])
        []
    """
    filtered_data = [
        int(cleaned) for element in data if (cleaned := element.strip()).isdigit()
    ]
    return filtered_data
