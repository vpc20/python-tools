from ColumnNumbers import print_col_numbers


def interval_bars(intvs):
    for stime, ftime in intvs:
        print(' ' * stime * 4, end='')
        print('|' + '-' * ((ftime - stime) * 4 - 1) + '|')


def interval_bars_same_line(intvs):
    prev_ftime = 0
    for stime, ftime in intvs:
        if prev_ftime == 0:
            print(' ' * stime * 4, end='')
        else:
            print(' ' * ((stime - prev_ftime) * 4 - 1), end='')
        print('|' + '-' * ((ftime - stime) * 4 - 1) + '|', end='')
        prev_ftime = ftime
    print('')


if __name__ == '__main__':
    print_col_numbers(101)
    # interval_bars([(0, 5), (3, 6), (6, 8)])
    # interval_bars([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)])
    # interval_bars([(1, 4), (5, 7), (8, 11), (12, 16)])
    # 0                                       1                                       2                                       3                                       4                                       5                                       6                                       7                                       8                                       9
    # 0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9   0   1   2   3   4   5   6   7   8   9
    # |-------------------|
    #             |-----------|
    #                         |-------|

    # intvs1 = [(5, 11), (5, 7), (1, 3), (1, 7), (1, 3), (9, 12), (9, 12), (11, 15), (12, 15), (12, 15)]
    intvs1 = [[3, 5], [9, 20]]
    interval_bars_same_line(intvs1)
    intvs2 = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    interval_bars_same_line(intvs2)
