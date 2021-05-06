animals = ['cat', 'dog', 'bird', 'monkey']
for animal in animals:
 print(f"{animal.upper()} is cool!")

for count in range(1,6):
 print(count)

numbers = list(range(1,6))
print(numbers)

deci = []
triples = []
for count in range(1,11):
    deci.append(count**3)
    triples.append(3**count)
print(f"{triples}\n{deci}")
