from print_matrix_data import print_matrix


def matrix_coordinates(m, n):
    """
    Print matrix coordinates (row, col)

    :param m: number of rows
    :param n: number of columns
    """
    return [[(i, j) for j in range(n)] for i in range(m)]


if __name__ == '__main__':
    print_matrix(matrix_coordinates(4, 4))
