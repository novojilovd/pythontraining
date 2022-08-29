import sys, os
readsize = 1024

def joining(fromfir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
            filepath = os.path.join(fromdir, filename)
            if not os.path.isfile(filepath): continue
            fileobj = open(filepath, 'rb')
            while True:
                filebytes = fileobj.read(readsize)
                if not filebytes: break
                output.write(filebytes)
            fileobj.close()
    output.close()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: joining.py [from-dir-name to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile = input('Name of file to be recreated? ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:3]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)

        try:
            joining(fromdir, tofile)
        except:
            print('Error joining files:')
            print(sys.exc_info[0], sys.exc_info[1])
        else:
            print('Joining complete, see ', absto)
        if interactive: input('Print Enter key')
