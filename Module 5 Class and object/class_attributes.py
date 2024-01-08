class Shop:
    cart = [] # is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer
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