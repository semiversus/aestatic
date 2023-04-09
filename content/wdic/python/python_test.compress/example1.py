# Schreibe ein Funktion, die ermittelt, ob ein String ein Palindrom ist (d.h.
# vorwärts und rückwärts das gleiche Wort ergibt)
def is_palindrom(word):
    """ Returns True, if the given word is a palindrom. Case should be ignored.
    >>> is_palindrom('Reittier')
    True
    >>> is_palindrom('Rakete')
    False

    :param word: string to be tested
    :returns: boolean
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
