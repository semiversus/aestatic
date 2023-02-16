# Schreibe eine Funktion, die angibt, ob die in einer Liste enthaltenen Zahlen
# streng fallend ist (jede Zahl muss kleiner der vorhergehenden sein)
def is_monotonic_falling(l):
    """ Check for monitonic falling numbers in a list
    >>> is_monotonic_falling([5, 4, 2, -1])
    True
    >>> is_monotonic_falling([3, 2, 1, 4])
    False

    :param l: the list to be checked
    :returns: boolean
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
