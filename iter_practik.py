class Car:

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"Model - {self.model}, Price : {self.price}"


class Garage:

    def __init__(self, name_garage):
        self.name_garage = name_garage
        self.car_list = []


    def add_car (self, car : Car):
        self.car_list.append(car)


    def __str__(self):
        car_info = '\n'.join(str(car) for car in self.car_list)
        return f"Garage {self.name_garage}, imeet takie ta4ki:\n{car_info}"


jiga = Car('kopeika', 500)
opel = Car('tigra', 2000)
daewoo = Car ('lanos', 3000)

alex_garage = Garage('Alex')
alex_garage.add_car(jiga)
alex_garage.add_car(opel)
alex_garage.add_car(daewoo)
print(alex_garage)