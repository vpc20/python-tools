import os


def create_test_dirs_files(parent_path, n):
    for i in range(1, n + 1):
        dirpath = os.path.join(parent_path, f'dir{str(i)}')
        os.makedirs(dirpath, exist_ok=True)
        for j in range(i):
            try:
                # f = open(os.path.join(dirpath, 'file' + str(i) + '-' + str(j + 1) + '.txt'), 'x')
                f = open(os.path.join(dirpath, f'file{str(i)}-{str(j + 1)}.txt'), 'x')
                f.write('test')
                f.close()
            except FileExistsError:
                pass

    print('Test directories and files has been created.')


create_test_dirs_files(r'c:\temp', 3)
