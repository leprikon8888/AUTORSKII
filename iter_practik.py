class Car:

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"Model - {self.model}, Price : {self.price}"


class CarIterator:

    def __init__(self, car_list):
        self.car_list = car_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.car_list):
            raise StopIteration
        temp_car = self.car_list[self.index]
        self.index += 1
        return temp_car


class Garage:

    def __init__(self, name_garage):
        self.name_garage = name_garage
        self.car_list = []

    def add_car(self, car: Car):
        self.car_list.append(car)

    def __str__(self):
        result = f"Garage {self.name_garage}: \n"
        for car in self.car_list:
            result += str(car) + "\n"
        return result

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.car_list):
                return self.car_list[index]
            else:
                raise IndexError('error index')

        if isinstance(index, slice):
            start = 0 if index.start is None else index.start
            stop = len(self.car_list) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step


            temp_car_list = []
            if start < 0 and stop >= len(self.car_list):
                raise IndexError
            for i in range(start, stop, step):
                temp_car_list.append(self.car_list[i])
            return temp_car_list

    def __len__(self):
        return  len(self.car_list)

    def __iter__(self):
        return CarIterator(self.car_list)


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


print('**************')
y = alex_garage[:]
for i in y:
    print(i)
print('**************')

for i in alex_garage:
    print(i)