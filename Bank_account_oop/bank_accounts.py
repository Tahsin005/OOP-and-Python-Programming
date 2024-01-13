class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initial_amount, accountName):
        self.balance = initial_amount
        self.name = accountName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposite complete.")
        self.getBalance()


    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTranser interrupted. ❌ {error}")

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\nDeposite complete.")
        self.getBalance()

class SavingAcct(InterestRewardAcct):
    def __init__(self, initial_amount, accountName):
        super().__init__(initial_amount, accountName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete:")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
