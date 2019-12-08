class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_vehicle_info(self):
        print(self.name, "is worth", self.price)


car = Vehicle("Car", 25000)
car.get_vehicle_info()
