import os
import shutil

# for dirpath, dirnames, filenames in os.walk(r"c:\go"):
#     for filename in filenames:
#         print(dirpath, dirnames, filenames)
#     break

import os
import shutil

parent_dir = r"c:\temp"
for dirpath, dirnames, filenames in os.walk(parent_dir):
    for filename in filenames:
        full_name = os.path.join(dirpath, filename)
        new_name = os.path.join(parent_dir, filename)
        if dirpath != parent_dir:
            print(f'Moving {filename}...')
            shutil.move(full_name, new_name)  # move one dir up
            if not os.listdir(dirpath):  # empty dir
                print(f'Remove dir {dirpath}...')
                os.rmdir(dirpath)  # remove dir
