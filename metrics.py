def average(data: list) -> float:
    """Calculates average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples.
        
    Returns:
        float: a floating point value representing the average of this list.
        
    Usage examples:
        >>> average([80, 90, 100])
        90.0

        >>> average([60, 75, 90, 105])
        82.5
    """
    if not data:
        return []
    
    average = sum(data) / len(data)
    return round(average, 2)


def maximum(data: list) -> float:
    """Calculates maximum value of the list

    Args:
        data (list[int]): list of integers representing heart rate samples.

    Returns:
        float: a floating point value representing the maximum of this list. 
        
    Usage examples:
        >>> maximum([80, 90, 100])
        100.0

        >>> maximum([60, 75, 90, 105])
        105.0
    """
    if not data:
        return []
    
    return float(max(data))


def variance(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population variance)
    """
    pass


def standard_deviation(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    pass
