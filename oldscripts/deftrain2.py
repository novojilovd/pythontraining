def cook(name_dish, count_dish=1):
    print(f"You ordered {count_dish}\n\tof {name_dish}\n")

print("Make your order\n(Write 'quit' to stop")
name_dish = ""
while True:
    name_dish = input("What do you want to eat?\n").lower()
    if name_dish == 'quit':
        break
    count_dish = input("How much?\n").lower()
    if count_dish == 'quit':
        break
    cook(name_dish.title(), int(count_dish))
