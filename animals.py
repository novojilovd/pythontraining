feline = ['cat', 'lynx', 'tyger', 'puma', 'occelot']
canine = ['dog', 'wolf', 'fox']
name = input("Write animal: ")
if name in feline:
    print(f'{name} is feline')
elif name in canine:
    print(f'{name} is canine')
else:
    print(f'{name} is not feline or canine')
