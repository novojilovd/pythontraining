def greet(name):
    if name == 'daniil':
        print(f"Hello {name.title()}")
    else:
        print(f"Hello not Daniil")

greet(input("Write your name ").lower().strip())
