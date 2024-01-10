class Product:
    def __init__(self) -> None:
        self.list_of_product = []
    
    def __repr__(self) -> None:
        for i in self.list_of_product:
            text = f'Name : {i['name']}, price : {i['price']} Quantity : {i['quantity']}, Weight : {i['weight']}'
            print(text)

class Shop(Product):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()
    
    def add_product(self, name, price, weight, quantity):
        self.name = name
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.list_of_product.append({'name' : self.name, 'price' : self.price, 'weight' : self.weight, 'quantity' : self.quantity})
    
    def buy_product(self, product_name, product_quantity, amount):
        i = 0
        idx = -1
        for pro in self.list_of_product:
            if pro['name'] == product_name:
                idx = i
            i += 1
        
        if idx == -1:
            print('Not in stock')
        else:
            cost = product_quantity * self.list_of_product[idx]['price']
            if cost < amount:
                amount -= cost
                print(f'Congratulations for buying {product_name}, price ({cost}). Here is your {amount} extra money')
            else:
                print(f'Not enough mone to buy {product_name}. Need {cost - amount} more to buy {product_name}')
general_store = Shop("M/S. Pahartali Super Shop")
general_store.add_product('potato', 90, 1, 100)
general_store.add_product('tomato', 120, 1, 200)
general_store.add_product('pencil', 10, 1, 100)

general_store.buy_product('potato', 3, 500)
general_store.buy_product('rice', 2, 100)
general_store.buy_product('tomato', 10, 100)