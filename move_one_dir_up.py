import os
import shutil

for dirpath, dirnames, filenames in os.walk(r"E:\The Handmaid's Tale"):
    for dirname in dirnames:
        for dirpath1, dirnames1, filenames1 in os.walk(os.path.join(dirpath, dirname)):
            for filename in filenames1:
                full_filename = os.path.join(dirpath1, filename)
                new_name = os.path.join(dirpath, filename)
                shutil.copyfile(full_filename, new_name)
                print(f'Copying {filename}...')
