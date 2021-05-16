class Animal():
    '''Training some functions'''

    def __init__(self, *args):

        self.text = [name for name in args]

    def output(self):
        for name in self.text: 
            print(f'{ name }', end=' ')
        print('\n')

    def help(self):
        print(f"You want to know { input('What do you want to know: ') }")

testing = Animal('Cat', 'Dog')

testing.output()
testing.help()
