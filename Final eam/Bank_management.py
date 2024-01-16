from random import randint

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = randint(10000, 99999)
        self.transaction_history = []
        self.loan_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded. Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

    def check_balance(self):
        return f"Available Balance: ${self.balance}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.deposit(amount)
            return f"Loan of ${amount} taken successfully."
        else:
            return "You have already taken the maximum number of loans."

    def transfer(self, amount, target_account):
        if target_account in accounts:
            if self.balance >= amount:
                self.balance -= amount
                target_user = accounts[target_account]
                target_user.deposit(amount)
                self.transaction_history.append(f"Transferred ${amount} to account {target_account}")
            else:
                print("Insufficient funds for the transfer.")
        else:
            print("Account does not exist.")

class Admin:
    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        accounts[user.account_number] = user
        return f"Account created successfully. Account number: {user.account_number}"

    def delete_account(self, account_number):
        if account_number in accounts:
            del accounts[account_number]
            return f"Account {account_number} deleted successfully."
        else:
            return "Account does not exist."

    def view_all_accounts(self):
        account_details = []
        for account_number, user in accounts.items():
            details = {
                "Account Number": account_number,
                "Name": user.name,
                "Email": user.email,
                "Address": user.address,
                "Account Type": user.account_type,
                "Balance": user.balance,
                "Loan Feature": user.loan_taken,
            }
            account_details.append(details)

        return account_details

    def check_total_balance(self):
        total_balance = sum(user.balance for user in accounts.values())
        return f"Total Available Balance: ${total_balance}"

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.loan_taken for user in accounts.values())
        return f"Total Loan Amount: ${total_loan_amount}"

    def toggle_loan_feature(self, status):
        User.loan_feature = status
        return f"Loan feature is now {'enabled' if status else 'disabled'}."

accounts = {}
User.loan_feature = True

def main():
    while True:
        print("\nBanking Management System\n")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                user = accounts[account_number]
                print(f"Welcome, {user.name}!")
                
                while True:
                    print("\nUser Menu\n")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Take Loan")
                    print("6. Transfer Money")
                    print("7. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        user.deposit(amount)
                        print("Deposit successful. Updated balance:", user.check_balance())

                    elif user_choice == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        user.withdraw(amount)

                    elif user_choice == '3':
                        print(user.check_balance())

                    elif user_choice == '4':
                        print("Transaction History:")
                        for transaction in user.check_transaction_history():
                            print(transaction)

                    elif user_choice == '5':
                        if User.loan_feature:
                            amount = float(input("Enter the loan amount: "))
                            print(user.take_loan(amount))
                        else:
                            print("Loan feature is currently disabled by the admin.")

                    elif user_choice == '6':
                        target_account = int(input("Enter the target account number: "))
                        amount = float(input("Enter the amount to transfer: "))
                        user.transfer(amount, target_account)

                    elif user_choice == '7':
                        break

            else:
                print("Invalid account number. Please try again.")

        elif choice == '2':
            admin = Admin()
            admin_password = input("Enter the admin password: ")

            if admin_password == "admin123":  # Change the password as needed
                print("Welcome, Admin!")

                while True:
                    print("\nAdmin Menu\n")
                    print("1. Create Account")
                    print("2. Delete Account")
                    print("3. View All Accounts")
                    print("4. Check Total Balance")
                    print("5. Check Total Loan Amount")
                    print("6. Toggle Loan Feature")
                    print("7. Logout")

                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        name = input("Enter user's name: ")
                        email = input("Enter user's email: ")
                        address = input("Enter user's address: ")
                        account_type = input("Enter account type (Savings/Current): ")
                        print(admin.create_account(name, email, address, account_type))

                    elif admin_choice == '2':
                        account_number = int(input("Enter the account number to delete: "))
                        print(admin.delete_account(account_number))

                    elif admin_choice == '3':
                        acc = admin.view_all_accounts()
                        for i in acc:
                            print(i)

                    elif admin_choice == '4':
                        print(admin.check_total_balance())

                    elif admin_choice == '5':
                        print(admin.check_total_loan_amount())

                    elif admin_choice == '6':
                        status = input("Enter 'enable' to enable or 'disable' to disable the loan feature: ")
                        if status.lower() == 'enable':
                            admin_status = True
                        elif status.lower() == 'disable':
                            admin_status = False
                        else:
                            print("Invalid input. Loan feature remains unchanged.")
                            continue
                        print(admin.toggle_loan_feature(admin_status))

                    elif admin_choice == '7':
                        break

            else:
                print("Invalid admin password. Please try again.")

        elif choice == '3':
            print("Thanks for trusting our service. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    main()
