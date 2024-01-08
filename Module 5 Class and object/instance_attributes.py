class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # instance attribute
    def add_to_cart(self, item):
        self.cart.append(item)
tahsin = Shop('tahsin ferdous')
tahsin.add_to_cart('rubik\' cube')
tahsin.add_to_cart('phone')

print(tahsin.cart)

ferdous = Shop('tahsin ferdous')
ferdous.add_to_cart('laptop')
ferdous.add_to_cart('cake')
print(ferdous.cart) 