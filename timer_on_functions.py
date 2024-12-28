import time


# --------------------------------------------------------------
# def transpose(matrix):
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#     return [[matrix[j][i] for j in range(nrows)] for i in range(ncols)]
#
#
# def transpose2(matrix):
#     return list(zip(*matrix))


# --------------------------------------------------------------
def rotate(matrix):  # clockwise
    nrows = len(matrix)
    ncols = len(matrix[0])
    return [[matrix[j][i] for j in range(nrows - 1, -1, -1)] for i in range(ncols)]


def rotate2(matrix):
    # Transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]

    # Reverse each row to get the rotated matrix
    rotated_matrix = [row[::-1] for row in transposed_matrix]

    return rotated_matrix


# --------------------------------------------------------------
# def flip_vertical(matrix):
#     nrows = len(matrix)
#     ncols = len(matrix[0])
#     return [[matrix[i][j] for j in range(ncols - 1, -1, -1)] for i in range(nrows)]
#
#
# def flip_vertical2(matrix):
#     return [row[::-1] for row in matrix]


# --------------------------------------------------------------
def flip_horizontal(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    # x = [[matrix[i][j] for j in range(ncols)] for i in range(nrows - 1, -1, -1)]
    return [[matrix[i][j] for j in range(ncols)] for i in range(nrows - 1, -1, -1)]


def flip_horizontal2(matrix):
    return [row for row in matrix[::-1]]


# --------------------------------------------------------------
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
for e in m:
    print(e)
print()

# --------------------------------------------------------------
# print(transpose(m))
# start = time.time()
# for _ in range(1000000):
#     transpose(m)
# end = time.time()
# print(end - start)
#
# print(transpose2(m))
# start = time.time()
# for _ in range(1000000):
#     transpose2(m)
# end = time.time()
# print(end - start)


# --------------------------------------------------------------
# print(rotate(m))
# start = time.time()
# for _ in range(1000000):
#     rotate(m)
# end = time.time()
# print(end - start)
#
# print(rotate2(m))
# start = time.time()
# for _ in range(1000000):
#     rotate2(m)
# end = time.time()
# print(end - start)


# --------------------------------------------------------------
# print(flip_vertical(m))
# start = time.time()
# for _ in range(1000000):
#     flip_vertical(m)
# end = time.time()
# print(end - start)
#
# print(flip_vertical2(m))
# start = time.time()
# for _ in range(1000000):
#     flip_vertical2(m)
# end = time.time()
# print(end - start)


# --------------------------------------------------------------
print(flip_horizontal(m))
start = time.time()
for _ in range(1000000):
    flip_horizontal(m)
end = time.time()
print(end - start)

print(flip_horizontal2(m))
start = time.time()
for _ in range(1000000):
    flip_horizontal2(m)
end = time.time()
print(end - start)
