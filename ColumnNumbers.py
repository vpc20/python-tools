# print(''.join([str(int(i / 10)) if i % 10 == 0 else ' ' for i in range(100)]))
# print(''.join([str(i) for i in range(10)]) * 10)


def print_0_to_9(ntimes, nspaces):
    for i in range(ntimes):
        print(''.join([str(i) + ' ' * nspaces for i in range(10)]), end='')
    print('')


def print_col_numbers(n):
    for i in range(0, n, 10):
        tens = i // 10
        print(f'{tens}{" " * (39 - (len(str(tens)) - 1))}', end='')
    print('')
    for i in range(n):
        print(f'{i % 10}   ', end='')
    print('')


def print_col_markers(n):
    for i in range(n // 10 + 1):
        print(f'{i}{" " * (10 - len(str(i)))}', end='')
    print('')
    for i in range(n + 1):
        if i == 0 or i % 10 == 0:
            print('0', end='')
        elif i % 5 == 0:
            print('+', end='')
        else:
            print('.', end='')
    print('')


if __name__ == '__main__':
    # print_0_to_9(1, 9)
    # print_0_to_9(10, 0)
    #
    # print_0_to_9(1, 39)
    # print_0_to_9(10, 3)
    #
    # print_0_to_9(1, 9)
    # print_0_to_9(10, 0)

    print_col_markers(132)
    print('')
    print_col_numbers(133)
