class UserException (Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message

num = int(input('input positove number: '))

try:
    if num < 0:
        raise UserException('Negative number ')
except UserException as err:
        print(err.get_exception_message())

print(num)