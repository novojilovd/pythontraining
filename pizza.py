toppings = ['cheese', 'mushrooms', 'meat', 'onions', 'pineapple', 'apple', 'fish', 'cacao', 'watermellon', 'candy']
count = int(input("How much toppings do you want?\n"))
order = "You add: "
for i in range(count):
    topping = input(f"What is your {i+1} topping?\n")
    if topping.lower() in toppings:
        print(f"Adding extra {topping.lower()}\n")
        order = order + f"{topping}, "
    else:
        print("We haven't this topping\n")

print("\nFinishing making your pizza!\n")
print(order[:-2],"!!!")
