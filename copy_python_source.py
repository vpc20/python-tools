import os
import shutil
# from zipfile import ZipFile


for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\PycharmProjects'):
    # print(dirpath, dirnames, filenames)
    # for dirname in dirnames:
    #     print(dirpath + '\\' + dirname)
    for filename in filenames:
        full_filename = dirpath + '\\' + filename
        if full_filename.endswith('.py') \
                and '__init__' not in full_filename \
                and '\\Lib\\' not in full_filename \
                and '\\Scripts\\' not in full_filename:
            new_dir = dirpath.replace('C:\\Users\\vpc\\', 'C:\\temp\\')
            try:
                os.makedirs(new_dir)
            except FileExistsError:
                pass
            new_name = full_filename.replace('C:\\Users\\vpc\\', 'C:\\temp\\')
            print(full_filename)
            shutil.copyfile(full_filename, new_name)

print('\nPython files copied to C:\\temp\\PycharmProjects')
# zipf = ZipFile(new_name)