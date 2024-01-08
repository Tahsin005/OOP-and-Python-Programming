class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000
    def get_balance(self):
        print(self.balance)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Forkira, you cannot withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'Bank fokir hoi jabe. you can not withdraw more than {self.max_withdraw}')
        else:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Here is your money {amount}')
            else:
                print('oi fokira.. tr eto taka nai..')
        
brac = Bank(15000)
brac.withdraw(10000) 
brac.get_balance()
brac.withdraw(4000)
brac.get_balance()
brac.withdraw(1500)
brac.get_balance()
