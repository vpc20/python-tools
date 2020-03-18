import sys


def print_matrix(arr):  # same width for each column, ideal when inspecting diagonals
    maxlen = max([len(str(n)) for subarr in arr for n in subarr])
    for subarr in arr:
        print('')
        for item in subarr:
            if isinstance(item, list):
                item = str(item)
            if type(item) is str:
                print(f'{item:{maxlen}}', end='  ')
            else:
                print(f'{str(item):>{maxlen}}', end='  ')  # right justify numbers
    print('')


def print_matrix1(arr):  # different width for each column
    maxlenarr = []
    for col in range(len(arr[0])):
        maxlencol = -sys.maxsize
        for row in range(len(arr)):
            maxlencol = max(maxlencol, len(str(arr[row][col])))
        maxlenarr.append(maxlencol)
    for row in range(len(arr)):
        print('')
        for col in range(len(arr[0])):
            item = arr[row][col]
            width = maxlenarr[col]
            if isinstance(item, list):
                item = str(item)
            if isinstance(item, str):
                print(f'{item:{width}}', end='  ')
            else:
                print(f'{str(item):>{width}}', end='  ')  # right justify numbers
    print('')


if __name__ == '__main__':
    # arr1 = [[22, 11, 2, 17, 24],
    #         [3, 16, 23, 12, 7],
    #         [10, 21, 6, 1, 18],
    #         [15, 4, 19, 8, 13],
    #         [20, 9, 14, 5, 0]]
    #
    # arr2 = [['asdf1', 'aaa', 'bb', 'ccc'],
    #         ['asdf2', 'a', 'b', 'ccc'],
    #         ['asdf3', 'a', 'bb', 'cc']]
    #
    # print_matrix(arr1)
    # print_matrix(arr2)
    #
    # print_matrix1(arr1)
    # print_matrix1(arr2)
    print_matrix1([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', '←', '←', '←', '←', '↖', '←', '←'], [' ', '↖', '←', '←', '←', '←', '←', '←'], [' ', '↖', '←', '←', '←', '←', '←', '←'], [' ', '↑', '←', '↖', '←', '←', '←', '←'], [' ', '↑', '←', '↑', '←', '↖', '←', '←'], [' ', '↑', '←', '↑', '←', '↑', '←', '↖']])
