import os

path = os.environ.get('PATH')
# in windows, the delimiter is ';', in linux it's ':'
delim = ';' if os.name == 'nt' else ':'
pathnames = sorted(path.split(delim))
pathnames = [pathname for pathname in pathnames if pathname != '']  # remove empty strings (due to double ;)
print(f'\nNo of paths in PATH environment variable: {len(pathnames)}')

print('\n-------------------------------------')
print('Values for PATH environment variable:')
for pathname in pathnames:
    print(f'  {pathname}')

print('\n------------------------------------')
print('Duplicate PATH environment variable:')

seen = set()
for pathname in pathnames:
    pathname = pathname.rstrip('/')
    if pathname in seen:
        print(f'  {pathname}')
    else:
        seen.add(pathname)

if len(seen) == len(pathnames):
    print('*** No duplicate paths ***')

print('\n')

# print(os.environ['PATH'])
# all_paths = ':'.join(seen)
# print(all_paths)
# os.environ['PATH'] = all_paths
