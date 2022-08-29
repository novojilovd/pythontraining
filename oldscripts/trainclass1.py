class Animal():
    '''Training some functions'''

    def __init__(self, *args):

        self.text = list(set([name for name in args]))
        self.count = [1 for i in range(len(self.text))]

    def output(self):
        for i in range(len(self.text)): 
            print(f'{ self.text[i] } {self.count[i]}')

    def help(self):
        print(f"You want to know { input('What do you want to know: ') }")

    def counting(self):
        for i in range(len(self.text)):
            self.count[i] = input(f'How much {self.text[i].lower()} do you have: ')

    def changing(self, name, count):
        for i in range(len(self.text)):
            if self.text[i] == name:
                self.count[i] = count
                break
                
                
testing = Animal('Cat', 'Dog', 'Cat')
testing.counting()
testing.output()
testing.changing('Cat', 5)
testing.output()
