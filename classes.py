class Pizza:
    def __init__(self, size, style, topping, order_complete):
        self.size = size
        self.style = style
        self.topping = topping
        self.order_complete = False


    def add_topping(self):
      self.topping = topping

    def print_order(self):
        self.order_complete = True
        print(f'I would like a {self.size} inch, {self.style} pizza with {self.topping}')

meat_lovers = Pizza(size = "16", style = "Deep Dish", topping = "Pepperoni", order_complete = "True")

meat_lovers = Pizza()
# meat_lovers.size = 16
# meat_lovers.style = "Deep dish"
# meat_lovers.add_topping("Pepperoni")
# meat_lovers.add_topping("Olives")
# meat_lovers.print_order()

for prop, value in meat_lovers.__dict__.items():
    print(f'{prop}:\n{value}\n')


print(meat_lovers.topping)
meat_lovers.print_order()
