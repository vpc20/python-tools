def transpose(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    return [[matrix[j][i] for j in range(nrows)] for i in range(ncols)]


# def rotate(matrix):
#     result = []
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#
#     for i in range(ncols):
#         result.append([])
#         for j in range(nrows - 1, -1, -1):
#             result[-1].append(matrix[j][i])
#     return result


def rotate(matrix):  # clockwise
    nrows = len(matrix)
    ncols = len(matrix[0])
    return [[matrix[j][i] for j in range(nrows - 1, -1, -1)] for i in range(ncols)]


def flip_vertical(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    return [[matrix[i][j] for j in range(ncols - 1, -1, -1)] for i in range(nrows)]


if __name__ == '__main__':

    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    for e in m:
        print(e)
    print()

    m1 = transpose(m)
    for e in m1:
        print(e)

    # m1 = rotate(m)
    # for e in m1:
    #     print(e)

    # m1 = flip_vertical(m)
    # for e in m1:
    #     print(e)
