favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'c++'
    }
friends = ['jen', 'jhon', 'edward']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
