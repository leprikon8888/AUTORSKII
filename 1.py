class Message:

    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def __str__(self):
        return f'Message [name = {self.sender}, text = {self.text}]'


b = Message('sasha', 'hello')
print(b)

a = Message('oleg', "biy")
print(a)