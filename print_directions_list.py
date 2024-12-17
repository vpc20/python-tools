LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

dirs = {1: (0, -1),
        2: (0, 1),
        3: (-1, 0),
        4: (1, 0)}

dirs2 = {1: '(r, c - 1)',
         2: '(r, c + 1)',
         3: '(r - 1, c)',
         4: '(r + 1, c)'}

dir_text = {1: 'left',
            2: 'right',
            3: 'up',
            4: 'down'}


def print_directions_list(dirlist):
    print('[', end='')
    for i, e in enumerate(dirlist):
        if i == len(dirlist) - 1:
            print(f'{dirs[e]}]  # ', end='')
        else:
            print(f'{dirs[e]}, ', end=' ')  # last direction in list

    for i, e in enumerate(dirlist):
        if i == len(dirlist) - 1:
            print(dir_text[e])
        else:
            print(dir_text[e], end=', ')  # last direction in list

    #  rows/column delta
    for i, e in enumerate(dirlist):
        if i == len(dirlist) - 1:
            print(f'{dirs2[e]}]  # ', end='')
        else:
            print(f'{dirs2[e]}, ', end=' ')  # last direction in list

    for i, e in enumerate(dirlist):
        if i == len(dirlist) - 1:
            print(dir_text[e])
        else:
            print(dir_text[e], end=', ')  # last direction in list


if __name__ == '__main__':
    print_directions_list([RIGHT, DOWN, LEFT, UP])
    # print_directions_list([UP, RIGHT, DOWN, LEFT])
