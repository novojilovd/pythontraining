class Restorane():
    '''Main class for all type of food'''

    def __init__(self, name = 'Floppation', workers = 1):
        self.name = name
        self.workers = workers
        self.menu = { 'Meat': 10, 'Fish': 10, 'Candy': 100 }

        print(f'Welcome to "{self.name}"!\n')
    
    def show_menu(self):
        print('Our menu:\n')
        i = 1
        for dish, price in self.menu.items():
            print(f'{ i }. { dish.title() } is cost { price } g.')
            i +=1

    def ordering(self, menu_title = 'Main menu'):
        print('\nMake your order, please.\nWrite "done" when you complete\n')
        order = {}
        while True:
            name_dish = input('Write what do you want to order: ').lower()
            if name_dish.lower() == 'done':
                break
            if name_dish.title() not in self.menu.keys():
               print("Sorry, we don't have it, order something else")
               continue
            else:
                count = int(input(f'How much { name_dish } do you want: '))
                print(f'You ordered { count } { name_dish }')
                order[name_dish] = count
        print(f'--- { menu_title } --- \nYour order:\n')
        for name, count in order.items():
            print(f'- { name } x { count } = { self.menu.get(name.title()) * count } g') 

class Bottle(Restorane):
    
    def __init__(self):
        self.menu = { 'Red Vine': 10, 'White Vine': 10, 'Blue Vine': 100, 'Glue Vine': 1000}
        self.history = { 'Red Vine': 'Good', 'White Vine': 'Bad', 'Blue Vine': 'Angry', 'Glue Vine': 'Glue'}        

    def drink_history(self, drink):
        print(f'{ self.history.get(drink.title()) }')

def food():
    test = Restorane(input("Which restorane do you want to visit?\n"), 10)
    test.show_menu()
    test.ordering()

def drink():
    test = Bottle()
    test.show_menu()
    test.drink_history('Red vine')
    test.ordering('Vine card')

food()
drink()
