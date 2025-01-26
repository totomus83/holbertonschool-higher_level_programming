'''
the matrix_divided function divides each element
of a matrix by the value of div
element of the matrix are rounded to 2 decimal float
raise error if requirement are not met
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of matrix by value of div
    '''
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix of integer or float")
    for row in matrix:
        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row must have the same size")
    newmatrix = []
    if div == float("inf"):
        newmatrix = [
            list(map(lambda x: 0.0, row))
            for row in matrix]
    else:
        newmatrix = [
            list(map(
                lambda x: round(x / div, 2) if x != -0.0 else 0.0, row))
            for row in matrix]
    return newmatrix
