animals = {
    'feline': 'cat',
    'canine': 'dog',
    'vulpine': 'fox',
    'floppa': 'floppa'
    }
name = input('What an animal do you want know? ')
if name.lower() == 'floppa':
    print('It is Floppa of course')
elif name.lower() in animals.values():
    print('Sorry, this code for values method training, not items method')
for key, value in animals.items():
    if value == name.lower():
        print(f"But it now, so it is {key}")
