def sum_2_values(x, y):

    """
    >>> sum(10, 20)
    30

    >>> sum(-10, 20)
    20
    """    

    assert isinstance(x, (int, float)), 'x needs to be int ou float'
    assert isinstance(y, (int, float)), 'y needs to be int ou float'
    return x + y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)