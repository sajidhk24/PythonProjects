class Item:
    pay_rate = 0.8  # The rebate of 20%
    all = []  # we can also create class method in instance using "@Classmethod" just above any method /
# in instance level

    def __init__(self, name: str, gadgets: str, cost: float, quantity: int):
        # Assertion of received arguments
        assert cost >= 0, f'{cost} cant be negative!'
        assert quantity >= 0, f'{quantity} cant be negative!'

        # Intense using class
        self.name = name
        self.type = gadgets
        self.cost = cost
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def total_cost(self):
        return self.cost * self.quantity

    def apply_discount(self):
        self.cost = self.cost * self.pay_rate

    def __repr__(self):
        return f'Item: {self.name, self.cost, self.quantity}'


item1 = Item('Apple', 'Laptop', 68000, 2)
item2 = Item('nokia', 'mobile', 2400, 200)
item3 = Item('Supreme', 'cable', 1500, 1)
item4 = Item('Apple_mouse', 'mouse', 700, 2)
item5 = Item('apple_keyboard', 'keyboard', 1200, 4)

print(item1)
print(item2)
print(item2.total_cost())
print(Item.__dict__)
print(item2.__dict__)
# print(Item.pay_rate)
# print(item1.pay_rate)
(item1.apply_discount())
print(item1.cost, '\n')
print(Item.all)
for instance in Item.all:
    print(instance.name)
