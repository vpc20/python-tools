# def print_matrix_vertical(arr2d):
#     maxlen = max([len(str(n)) for subarr in arr2d for n in subarr])
#     print('[', end='')
#     for i, subarr in enumerate(arr2d):
#         # print('')
#         for j, item in enumerate(subarr):
#             if j == 0:
#                 if i == 0:
#                     print('[', end='')
#                 else:
#                     print(' [', end='')
#             if type(item) is str:
#                 if j == len(subarr) - 1:
#                     print(f'{item:{maxlen}}', end=' ')
#                 else:
#                     print(f'{item:{maxlen}},', end=' ')
#             else:
#                 if j == len(subarr) - 1:
#                     print(f'{str(item):>{maxlen}}', end=' ')  # right justify numbers
#                 else:
#                     print(f'{str(item):>{maxlen}},', end=' ')
#             if j == len(subarr) - 1:
#                 if i == len(arr2d) - 1:
#                     print(']', end='')
#                 else:
#                     print('],')
#     print(']')


def print_matrix_vertical(arr2d):
    maxlen = max([len(str(n)) for subarr in arr2d for n in subarr])
    print('[', end='')
    for i, subarr in enumerate(arr2d):
        # print('')
        for j, item in enumerate(subarr):
            if j == 0:
                if i == 0:
                    print('[', end='')
                else:
                    print(' [', end='')

            # if j == len(subarr) - 1:
            #     print(f'{str(item):>{maxlen}}', end=' ')  # right justify numbers
            # else:
            #     print(f'{str(item):>{maxlen}},', end=' ')
            if isinstance(item, str):  # enclose strings in single qoutes
                item = "'" + item + "'"

            if isinstance(item, int) or isinstance(item, float):
                item_fstr = f'{item:>{maxlen}}'  # right justify numbers
            else:
                item_fstr = f'{str(item):{maxlen}}'

            if j < len(subarr) - 1:
                item_fstr += ','

            print(item_fstr, end=' ')

            if j == len(subarr) - 1:
                if i == len(arr2d) - 1:
                    print(']', end='')
                else:
                    print('],')
    print(']')


if __name__ == '__main__':
    # arr2d = [[[()], []], [[()], [('a',)]]]
    # print_matrix_vertical(arr2d)
    # print_matrix_vertical([[[()], [], []], [[()], [('a',)], []], [[()], [('a',), ('b',)], [('a', 'b'), ('b', 'a')]], [[()], [('a',), ('b',), ('c',)], [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b')]], [[()], [('a',), ('b',), ('c',), ('d',)], [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b'), ('a', 'd'), ('d', 'a'), ('b', 'd'), ('d', 'b'), ('c', 'd'), ('d', 'c')]]])
    print_matrix_vertical([['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al'],
                           ['ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl'],
                           ['ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl'],
                           ['da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl'],
                           ['ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el'],
                           ['fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl'],
                           ['ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl'],
                           ['ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh', 'hi', 'hj', 'hk', 'hl'],
                           ['ia', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'ih', 'ii', 'ij', 'ik', 'il'],
                           ['ja', 'jb', 'jc', 'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl'],
                           ['ka', 'kb', 'kc', 'kd', 'ke', 'kf', 'kg', 'kh', 'ki', 'kj', 'kk', 'kl'],
                           ['la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll']])
    print_matrix_vertical([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                           [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33],
                           [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44],
                           [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
                           [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66],
                           [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77],
                           [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88],
                           [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],
                           [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
                           [0, 11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121]])
