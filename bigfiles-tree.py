import sys, os ,pprint
trace = True
if sys.platform.startswith('lin'):
    dirname = '/usr/lib/python3.6'
else:
    dirname = r'C:\Python36\Lib'
print(dirname)
allsizes = []
for (paths, directorys, files) in os.walk(dirname):
    if trace: print(paths)
    for filename in files:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(paths, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
