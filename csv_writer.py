import csv

a = [[(i, j) for j in range(5)] for i in range(5)]
# a = [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)], [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)], [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)], [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)], [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)], [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)], [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)], [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]]


# write all rows
with open("temp.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(a)

# write single row
with open("temp1.csv", "a", newline='') as csvf:
    csv_writer = csv.writer(csvf)
    csv_writer.writerow(a[0])

# arr = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]], [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2]], [[0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2]], [[0, 1, 1, 1], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 2], [0, 1, 2, 3], [0, 1, 2, 3]], [[0, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3], [1, 2, 3, 3], [1, 2, 3, 3], [1, 2, 3, 4]]]
# with open("oneszeroes.csv", "w", newline='') as f:
#     writer = csv.writer(f)
#     for e in arr:
#         writer.writerows(e)

# with open("longestvalidparen.csv", "a", newline='') as csvf:
#     csv_writer = csv.writer(csvf)
#     csv_writer.writerow([0, 2])
#     csv_writer.writerow([0, 2, 0, 4])
#     csv_writer.writerow([0, 2, 0, 4, 0, 6])
#     csv_writer.writerow([0, 0, 2, 4])
#     csv_writer.writerow([0, 0, 0, 2, 4, 6])
#     csv_writer.writerow([0, 2, 0, 0, 0, 2, 4, 8])

with open("tempx.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(
        [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 2, 2, 2, 2, 2], [0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 1, 2, 2, 3, 3, 4]]
        )
