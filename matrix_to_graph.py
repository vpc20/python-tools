from collections import defaultdict


# using coordinates (r, c) as nodes
def matrix_to_graph(arr):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(arr)
    ncols = len(arr[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    g[(r, c)].append((nr, nc))
    return g


# using data as nodes, value should be unique
def matrix_to_graph1(arr):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(arr)
    ncols = len(arr[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    g[arr[r][c]].append(arr[nr][nc])
    return g


# case where there are duplicate data in grid
# AAAA
# BBCD
# BBCC
# EEEC
def matrix_to_graphx(arr):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(arr)
    ncols = len(arr[0])

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if arr[r][c] == arr[nr][nc]:
                        g[(r, c)].append((nr, nc))
            else:
                _ = g[(r, c)]  # create empty list, use _ instead of dummy variable
    return g


if __name__ == '__main__':
    arr = [['a', 'b', 'c', 'd', 'e'],
           ['f', 'g', 'h', 'i', 'j'],
           ['k', 'l', 'm', 'n', 'o']]
    g = matrix_to_graph(arr)
    for k, v in g.items():
        print('key', k, ' val', v)

