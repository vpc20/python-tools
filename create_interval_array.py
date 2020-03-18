from ColumnNumbers import print_0_to_9


def create_intv_arr(text):
    intvn = -1
    intvs = []
    for line in text.split('\n'):
        stime = -1  # start time
        ftime = -1  # finish time
        for i, c in enumerate(line):
            if c == '|':
                if stime == -1:
                    stime = i
                else:
                    ftime = i
                    intvn += 1
                    intvs.append((stime, ftime, chr(intvn + 97)))
                    stime = -1
                    ftime = -1
    return intvs


def disp_intv_sep(intvs):
    print_0_to_9(1, 9)
    print_0_to_9(10, 0)
    for st, ft, _ in intvs:
        print(' ' * st, end='')
        print('|', end='')
        print('-' * (ft - st - 1), end='')
        print('|', end='')
        print('')


def disp_intv(intvs):
    print_0_to_9(1, 9)
    print_0_to_9(10, 0)
    prev_ft = -1
    for i, (st, ft, _) in enumerate(intvs):
        if st != prev_ft:
            print(' ' * (st - prev_ft - 1), end='')
            print('|', end='')
        print('-' * (ft - st - 1), end='')
        print('|', end='')
        prev_ft = ft
        if i < len(intvs) - 1 and intvs[i + 1][0] < intvs[i][1]:
            print('')  # new line
            prev_ft = -1
    print('')


t = '''
           |------------------|        |------|
|-----|    |----|        |----------| 
|---------------|                 |-----------|
|-----|                  |----------|  |------|
'''

intvs = create_intv_arr(t)
print(intvs)

print('print intervals')
disp_intv_sep(intvs)

print('sorted by start time')
disp_intv_sep(sorted(intvs))

print('sorted by finish time')
disp_intv_sep(sorted(intvs, key=lambda e: e[1]))

print('sorted by duration')
disp_intv_sep(sorted(intvs, key=lambda e: e[1] - e[0]))

# print_0_to_9(1, 9)
# print_0_to_9(10, 0)
# disp_intv_arr(intvs)

intvs = [(0, 6, 'c'), (11, 16, 'd'), (25, 36, 'e'), (39, 46, 'b'), (0, 6, 'h'), (11, 30, 'a'), (34, 46, 'g'),
         (0, 16, 'f'), (25, 36, 'i'), (39, 46, 'j')]
disp_intv(intvs)

# intvs = [(0, 1, 'b'), (1, 3, 'a'), (3, 6, 'c')]
intvs = [(0, 5, 'b'), (5, 10, 'b'), (10, 20, 'b')]
disp_intv(intvs)
