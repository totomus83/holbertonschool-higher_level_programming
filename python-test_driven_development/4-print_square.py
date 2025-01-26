'''
print_square prints a square with # of size size
if requirement are not met
'''


def print_square(size=None):
    '''
    prints a square of size size with #
    '''
    if size is None:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
