from print_matrix_data import print_matrix
from print_matrix_vertical import print_matrix_vertical


def create_matrix(m, n, nums=True):
    """
    Create a sample matrix with m rows and n columns

    :param nums: numeric sample data when True
    :param m: number of rows
    :param n: number of columns
    """
    arr2d = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if nums:
                arr2d[i].append(i * j)
            else:
                arr2d[i].append(chr(i + 97) + chr(j + 97))
    return arr2d


if __name__ == '__main__':
    # arr = create_matrix(12, 12, False)
    arr = create_matrix(12, 12)
    print(arr)
    print_matrix(arr)
    print('')
    print_matrix_vertical(arr)
