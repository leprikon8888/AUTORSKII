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
        result = f"Garage {self.name_garage}: \n"
        for car in self.car_list:
            result+=str(car) + "\n"
        return result



    def __getitem__(self, index):
        if isinstance(index, int):
            if index>=0 and index<len(self.car_list):
                return self.car_list[index]
            else:
                raise IndexError ('nepravilnui index')


        # if isinstance(index, slice):
        #     return self.car_list[slice]
        # else:
        #     raise  ValueError('vvedi 4toto korrektnoe')
        # # index = 0
        # if index<len(self.car_list):
        #     return self.car_list[index]
        #     index+=1
        # else:
        #     raise IndexError
        # ...

    def __len__(self):
        ...


jiga = Car('kopeika', 500)
opel = Car('tigra', 2000)
daewoo = Car ('lanos', 3000)

alex_garage = Garage('Alex')
alex_garage.add_car(jiga)
alex_garage.add_car(opel)
alex_garage.add_car(daewoo)
alex_garage.add_car(jiga)
alex_garage.add_car(opel)
alex_garage.add_car(daewoo)
print (alex_garage[:])