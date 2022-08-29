import os, sys, pprint
trace = 0

visited = {}
allsizes = []
for srcdir in sys.path:
    for (paths, directorys, files) in os.walk(srcdir):
        if trace > 0: print(paths)
        paths = os.path.normpath(paths)
        fixcase = os.path.normcase(paths)
        if fixcase in visited:
            continue
        else:
            visited[fixcase] = True
        for filename in files:
            if filename.endswith('.py'):
                if trace > 1: print('...', filename)
                pypath = os.path.join(paths, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except os.error:
                    print('skipping', pypath, sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((pysize, pylines, pypath))

print('By size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

print('By lines...')
allsizes.sort(key=lambda x: x[1])
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
