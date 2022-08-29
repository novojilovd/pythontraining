def more(text, numlines=15):
    try:
        while text:
            for i in range(numlines):
                print(text.readline())
            if text and input('More?') not in ['y', 'Y']: break
    except:
        print('No text')

def grail(x):
    raise TypeError('one')

if __name__ == '__main__':
    import traceback, sys
    #more(open(sys.argv[0]), 5)
    try:
        grail('Daniil')
    except:
        exc_info = sys.exc_info()
        print(exc_info[0])
        print(exc_info[1])
        traceback.print_tb(exc_info[2])