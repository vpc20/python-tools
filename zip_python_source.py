import os
from zipfile import ZipFile

py_zipf = ZipFile(r'C:\Users\vpc\Documents\MuseScore3\Scores\PycharmProjects.zip', mode='w')
kot_zipf = ZipFile(r'C:\Users\vpc\Documents\MuseScore3\Scores\KotlinProjects.zip', mode='w')
# andr_zipf = ZipFile(r'C:\Users\vpc\Documents\MuseScore3\Scores\AndroidStudioProjects.zip', mode='w')

for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\PycharmProjects'):
    for filename in filenames:
        fullname = dirpath + '\\' + filename
        if fullname.endswith('.py') \
                and '__init__' not in fullname \
                and '\\Lib\\' not in fullname \
                and '\\Scripts\\' not in fullname:
            print(f'zipping {fullname}...')
            py_zipf.write(fullname)
print('\nPython files zipped.')

for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\KotlinProjects'):
    for filename in filenames:
        fullname = dirpath + '\\' + filename
        if fullname.endswith('.kt'):
            print(f'zipping {fullname}...')
            kot_zipf.write(fullname)

print('\nKotlin files zipped.')

# for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\AndroidStudioProjects'):
#     for filename in filenames:
#         fullname = dirpath + '\\' + filename
#         if fullname.endswith('.kt'):
#             print(f'zipping {fullname}...')
#             andr_zipf.write(fullname)
#
# print('\nAndroid projects zipped.')
