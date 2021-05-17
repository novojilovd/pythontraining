class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can' roll back odometer!")

    def increment_odometer(self, miles):
        self.idometer_reading += miles

    def fill_gas_tank(self):
        print('Filled')

class ElectricCar(Car):

    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery_size = 175

    def battery_describe(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas!")

my_car = Car('volvo', 'model b', 2099)
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery_describe()
my_car.fill_gas_tank()
my_tesla.fill_gas_tank()
