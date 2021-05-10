def greet(name):
    if name.lower().split() == 'daniil':
        print(f"Hello {name.upper()}")
    else:
        print(f"Hello not Daniil")

greet(input("Write your name "))
