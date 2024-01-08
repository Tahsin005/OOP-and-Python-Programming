class Phone:
    price = 19000
    color = 'blue'
    brand = 'samsung'
    feature = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to : {phone} and message : {sms}'
        return text
myphone = Phone()
print(myphone)
print(myphone.price)
print(myphone.color)
print(myphone.brand)
myphone.call()
res = myphone.send_sms(1310091260, 'Hello World! from python')
print(res)