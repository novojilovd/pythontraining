def more(text, numlines=15):
    try:
        while text:
            for i in range(numlines):
                print(text.readline())
            if text and input('More?') not in ['y', 'Y']: break
    except:
        print('No text')
if __name__ == '__main__':
    import sys
    more(open(sys.argv[0]), 5)