def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


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
