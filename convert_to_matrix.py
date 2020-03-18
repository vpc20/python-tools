from print_matrix_data import print_matrix
from print_matrix_vertical import print_matrix_vertical


def conv_to_matrix(arr, ncol):
    """
    Convert single dimension array to 2d

    :param arr: input array
    :param ncol: number of columns in 2d array
    :return:
    """
    arr2d = [[] * ncol for _ in range(ncol)]
    for i in range(len(arr)):
        row = int(i / ncol)
        arr2d[row].append(arr[i])
    return arr2d


if __name__ == '__main__':
    # sample is the knight's tour possible solutions from each starting position
    arr = [304, 0, 56, 0, 304, 0, 56, 0, 56, 0, 56, 0, 64, 0, 56, 0, 56, 0, 56, 0, 304, 0, 56, 0, 304]
    a1 = conv_to_matrix(arr, 5)
    print_matrix(a1)
    print('')
    print_matrix_vertical(a1)
