# def transpose(matrix):
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#     return [[matrix[j][i] for j in range(ncols)] for i in range(nrows)]


def transpose(matrix):  # much faster than function above
    return list(zip(*matrix))


# def rotate_clockwise(matrix):
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#     return [[matrix[j][i] for j in range(nrows - 1, -1, -1)] for i in range(ncols)]


def rotate_clockwise(matrix):
    # Transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]
    # Reverse each row to get the rotated matrix (flip vertically)
    rotated_matrix = [row[::-1] for row in transposed_matrix]

    return rotated_matrix


def rotate_counter_clockwise(matrix):
    # Flip the matrix vertically
    flipped_vertical_matrix = [row[::-1] for row in matrix]

    # Transpose to get the rotated matrix
    rotated_matrix = list(zip(*flipped_vertical_matrix))

    return rotated_matrix


# def flip_vertical(matrix):
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#     return [[matrix[i][j] for j in range(ncols - 1, -1, -1)] for i in range(nrows)]


def flip_vertical(matrix):
    return [row[::-1] for row in matrix]


# def flip_horizontal(matrix):
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#     # x = [[matrix[i][j] for j in range(ncols)] for i in range(nrows - 1, -1, -1)]
#     return [[matrix[i][j] for j in range(ncols)] for i in range(nrows - 1, -1, -1)]


def flip_horizontal(matrix):
    return [row for row in matrix[::-1]]


if __name__ == '__main__':

    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    for e in m:
        print(e)
    print()

    # m1 = transpose(m)
    # for e in m1:
    #     print(e)

    m1 = rotate_clockwise(m)
    for e in m1:
        print(e)
    print()

    m1 = rotate_counter_clockwise(m)
    for e in m1:
        print(e)
    print()

    # m1 = flip_vertical(m)
    # for e in m1:
    #     print(e)

    # m1 = flip_horizontal(m)
    # for e in m1:
    #     print(e)

    m1 = transpose(m)
    for e in m1:
        print(e)
    print()
