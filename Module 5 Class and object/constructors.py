class Phone:
    manufactured = 'China'

    def __init__(self, brand, price, owner):
        self.owner = owner
        self.brand = brand
        self.price = price
    def send_sms(self, phone, sms):
        text = f'Sending to : {phone} {sms}'
        print(text)

myphone = Phone('asus' ,123, 'tahsin')
print(myphone.owner, myphone.brand, myphone.price)