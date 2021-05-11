class Dog():
    
    def __init__(self, age, *name):
        self.name = [i for i in name]
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog(6, 'wille', 'Jessi')

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.\n")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog(10, 'my', 'dog')
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.\n")
your_dog.sit()
your_dog.roll_over()
