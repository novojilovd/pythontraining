toppings = ['cheese', 'mushrooms', 'meat', 'onions', 'pineapple', 'apple', 'fish', 'cacao', 'watermellon', 'candy']
count = int(input("How much toppings do you want?\n"))
requested_toppings = []
for i in range(count):
    topping = input(f"What is your {i+1} topping?\n")
    if topping.lower() in toppings:
        requested_toppings.append(topping)
        print(f"Adding extra {topping.lower()}\n") 
    else:
        print("We haven't this topping\n")

print("\nFinishing making your pizza!")
