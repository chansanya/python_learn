class Car:

    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def run(self):
        print(f"传统车:{self.brand} {self.model} 类型:{self.type}")


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size


class ElectricCar(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model, '电动车')
        self.battery = Battery()

    def run(self):
        print(f"新能源:{self.brand} {self.model} 类型:{self.type},剩余电量:{self.battery.battery_size}")




