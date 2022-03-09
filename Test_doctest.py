def fact(n):
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    362880 
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    assert n > 1, 'n is not greater than 1'  # 断言
    return n * fact(n - 1)
if __name__ == '__main__':
    import doctest
    doctest.testmod()