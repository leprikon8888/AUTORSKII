class Message:

    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def __str__(self):
        return f'Message [name = {self.sender}, text = {self.text}]'


class Box_messages:

    def __init__(self):
        self.messages = []

    def add_message (self, message):
        self.messages.append(message)

    def get_last_message (self):
        if len(self.messages) == 0:
            return  None
        else:
            message = self.messages[-1]
            return message

    def __str__(self):
        res = ""
        for message in self.messages:
            res+= str(message)+'\n'
        return res



b = Message('sasha', 'hello')
a = Message('oleg', "biy")
c = Message('ivan', 'Python')

box = Box_messages()
box.add_message(a)
box.add_message(c)
box.add_message(b)

print(box)
m3 = box.get_last_message()
print(m3)