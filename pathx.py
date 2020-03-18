import os

path = os.environ.get('PATH')
pathnames = sorted(path.split(';'))
print('-' * 80)
print('Number of paths defined: ' + str(len(pathnames)))

print('Values for PATH environment variable:')
for pathname in pathnames:
    print(pathname)
