import os

for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\PycharmProjects'):
    # print(dirpath, dirnames, filenames)
    # for dirname in dirnames:
    #     print(dirname)
    for filename in filenames:
        if filename.startswith('temp') \
                and filename.endswith('text_to_matrix.py') \
                and 'site-packages' not in dirpath:
            print(f'{dirpath}\\{filename}')
