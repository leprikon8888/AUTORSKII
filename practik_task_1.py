class NegativeNumberError (Exception):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def __str__(self):
        return f'Input positive number'


while True:
    try:
        number = int(input(' enter how much money you want to receive '))
        if number <0:
            raise NegativeNumberError (number)
        break
    except ValueError:
        print("enter an integer that is equal to the sum")
    except NegativeNumberError as err:
        print (err, "  ", err.number)

print(number)