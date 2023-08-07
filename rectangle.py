class Rectangle:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area (self):
        return self.a * self.b

    def __str__(self):
        return f'Rectangle: length - {self.a},  width - {self.b} '


rec1 = Rectangle(2,3)
rec2 = Rectangle(3,6)
rec3 = Rectangle(5,2)
print(rec3)
print(rec3.area())
print(rec2.area())