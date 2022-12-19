import math


def calc_area_rectangle(x, y):
    """calculates the area of a rectangle

    Args:
        x (float): width of a rectangle
        y (float): length of a rectangle

    Raises:
        TypeError: Type Error when width is inputted as a string
        TypeError: Type Error when length is inputted as a string

    Returns:
        float: Area of a rectangle
    """

    if isinstance(x, str):
        raise TypeError("Only integers and floats allowed")
    elif isinstance(y, str):
        raise TypeError("Only integers and floats allowed")
    else:
        return x * y


def calc_area_circle(radius):
    """calculates the area of a circle

    Args:
        radius (float): radius of the circle

    Raises:
        TypeError: Type Error when radius is inputted as a string

    Returns:
        float: area of a circle
    """

    if isinstance(radius, str):
        raise TypeError("Only integers and floats allowed")
    else:
        return math.pi * (radius) ** 2
