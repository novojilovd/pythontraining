class Restorane():
    '''Main class for all type of food'''

    def __init__(self, name = 'Floppation', workers = 1):
        self.name = name
        self.workers = workers
        self.menu = { 'Meat': 10, 'Fish': 10, 'Candy': 100 }
    
    def show_menu(self):
        print('Our menu:\n')
        i = 1
        for dish, price in self.menu.items():
            print(f'{ i }. { dish.title() } is cost { price } g.')

    def ordering(self):
        print('Make your order, please.\nWrite "done" when you complete')
        while True:
            name_dish = input('Write what do you want to eat: ').lower()
            if name_dish.lower() == 'done':
                break
            if name_dish.title() not in self.menu.keys():
               print("Sorry, we don't have it, order something else")
               continue
            else:
                count = input(f'How much { name_dish } do you want: ')
                print(f'You ordered { count } { name_dish }')

test1 = Restorane('Hwllo', 10)
test1.show_menu()
test1.ordering()
         
