text = input('Write random string: ')
example = ''
for i in range(len(text)):
    example = example + chr((ord(text[i])+10))
text = example
example = ''
print(text)
