class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total price : ', total)  

        if total <= amount:
            print('Thanks for the payment')
        else:
            print(f'Please provide {total - amount} more')
    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
tahsin = Shopping('MD. Tahsin Ferdous')
tahsin.add_to_cart('alu', 90, 4)
tahsin.add_to_cart('dim', 12, 24)
tahsin.add_to_cart('rice', 50, 5)
print(tahsin.cart)

tahsin.checkout(600)

tahsin.remove_from_cart({'item' : 'alu', 'price' : 90, 'quantity' : 4})
print(tahsin.cart)