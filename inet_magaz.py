class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product : name = {self.name}, price = {self.price}'

p_1 = Product('kiwi', 9)
p_2 = Product('banana', 15)
p_3 = Product('kola', 75)
p_4 = Product('cherry', 54)
print(p_2)
print(p_3)


class Buyer:

    def __init__(self, name, surname, tel):
        self.name = name
        self.surname = surname
        self.tel = tel

    def __str__(self):
        return f'Buyer : name = {self.name}, surname = {self.surname},  telefon number = {self.tel}'

b_1 = Buyer('Ivan', 'Ivanov', '2-34-55')
b_2 = Buyer('Petr', 'Petrov', '873455')


class Order:

    def __init__(self, buyer:Buyer):
        self.buyer = buyer
        self.prod= []


    def add_product(self, product, quantity = 1):
        self.prod.append((product, quantity))

    def calculate(self):
        total = 0
        for product, quantity in self.prod:
            total+= product.price * quantity
        return total



    def __str__(self):
        order_info = f"Order for {self.buyer}:\n"
        for product, quantity in self.prod:
            coast = product.price * quantity
            order_info += f'{product.name}, quantity : {quantity}, coast : {coast}\n'
        order_info+=f"Total coast = {self.calculate()}"
        return order_info


zakaz_1 = Order(b_1)
zakaz_1.add_product(p_2, 5)
zakaz_1.add_product(p_1)
print(zakaz_1)

zakaz_2 = Order(b_2)
zakaz_2.add_product(p_4, 5)
zakaz_2.add_product(p_3, 2)
print(zakaz_2)