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

os.makedirs(r'c:\temp\dir1', exist_ok=True)
os.makedirs(r'c:\temp\dir2', exist_ok=True)
os.makedirs(r'c:\temp\dir3', exist_ok=True)

os.makedirs(r'c:\temp\dir1\dir1a', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1b', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1c', exist_ok=True)

os.makedirs(r'c:\temp\dir2\dir2a', exist_ok=True)
os.makedirs(r'c:\temp\dir2\dir2b', exist_ok=True)
os.makedirs(r'c:\temp\dir2\dir2c', exist_ok=True)

os.makedirs(r'c:\temp\dir3\dir3a', exist_ok=True)
os.makedirs(r'c:\temp\dir3\dir3b', exist_ok=True)
os.makedirs(r'c:\temp\dir3\dir3c', exist_ok=True)


os.makedirs(r'c:\temp\dir1\dir1a\dir1a1', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1a\dir1a2', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1a\dir1a3', exist_ok=True)

os.makedirs(r'c:\temp\dir1\dir1a\dir1a1/dir1a1x', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1a\dir1a2/dir1a2x', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1a\dir1a3/dir1a3x', exist_ok=True)
os.makedirs(r'c:\temp\dir1\dir1a\dir1a3/dir1a3y', exist_ok=True)

