class Goods:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Goods [name = {self.name}, price = {self.price}]'

class BasketIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index += 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Basket:

    def __init__(self, user):
        self.user = user
        self.goods_list = []

    def add_goods(self, goods: Goods):
        self.goods_list.append(goods)

    def __str__(self):
        res = f'User {self.user}\n'
        for good in self.goods_list:
            res += str(good) + '\n'
        return res

    def __iter__(self):
        return BasketIterator(self.goods_list)


user_basket_1 = Basket('Alex')

y = Goods('kivi', 8)
x = Goods('orange', 5)
z = Goods('apple', 28)
v = Goods('lime', 15)
user_basket_1.add_goods(x)
user_basket_1.add_goods(y)
user_basket_1.add_goods(z)
user_basket_1.add_goods(v)


for good in user_basket_1:
    print(good)
