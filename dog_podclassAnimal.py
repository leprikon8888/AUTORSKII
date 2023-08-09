class Animal:

    def __init__(self, age, ration, color):
        self.age = age
        self.ration = ration
        self.color = color


    def get_voice(self ):
        pass


    def __str__(self):
        return f'Animal: \n Age = {self.age}\n Ration = {self.ration}\n Color = {self.color}'



class Cat(Animal):

    def __init__(self, age, ration, color, name, cat_type):
        super().__init__(age, ration, color)
        self.name = name
        self.cat_type = cat_type


    def get_voice(self):
        return 'MEOW!!!'

    def __str__(self):
        return f'{super().__str__()}\n Name = {self.name}\n Cat_type = {self.cat_type}'



class Dog(Animal):

    def __init__(self ,age, ration, color, name, dog_type):
        super().__init__(age, ration, color)
        self.name = name
        self.dog_type = dog_type

    def get_voice(self):
        return "GAV!GAV!"

    def __str__(self):
        return f"{super().__str__()}\n Name = {self.name}\n Dog_type = {self.dog_type}"


bird = Animal(2, 'bread', 'black')
print(bird)

vaska = Cat(4, 'fish', 'white', "Vas`ka", 'home_cat')
print(vaska.get_voice())

sharik = Dog(6, 'meat', 'black', 'Sharik', 'hunter dog')
print(sharik)
print(sharik.get_voice())