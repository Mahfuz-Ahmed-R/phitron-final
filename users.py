from abc import ABC
import random

class User(ABC):
    def __init__(self, name, age, phone, address):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, age, phone, address, account_type):
        super().__init__(name, age, phone, address)
        self.account_type = account_type
        self.balance = 0
        self.transactions = []
        self.loan_count = 0
        self.account_number = random.randint(1000, 9999)

    def deposit(self, bank, amount):
        bank.deposit(self, amount)

    def withdraw(self, bank, amount):
        bank.withdraw(self, amount)

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def transaction_history(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, bank):
        if bank.loan_status:
            if self.loan_count < 2:
                loan_amount = int(input("Enter loan amount: "))
                self.balance += loan_amount
                self.loan_count += 1
                self.transactions.append(f"Took loan of {loan_amount}")
                bank.total_loan += loan_amount
                print("Loan granted")
            else:
                print("Cannot take more than two loans")
        else:
            print("Loan feature is currently off")

    def transfer_money(self, bank, to_acc_no, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            to_account = bank.find_account(to_acc_no)
            if to_account is None:
                print("Account does not exist")
            else:
                self.balance -= amount
                to_account.balance += amount
                self.transactions.append(f"Transferred {amount} to {to_account.name}")
                to_account.transactions.append(f"Received {amount} from {self.name}")
                print("Transfer successful")

class Admin(User):
    def __init__(self, name, age, phone, address):
        super().__init__(name, age, phone, address)

    def create_account(self, bank, customer):
        bank.customers.append(customer)
        print(f"Account created for {customer.name}")

    def delete_account(self, bank, account_number):
        account = bank.find_account(account_number)
        if account is None:
            print("Account not found")
        else:
            bank.customers.remove(account)
            print("Account deleted")

    def all_user_list(self, bank):
        bank.all_user_list()

    def total_balance(self, bank):
        print(f"Total bank balance: {bank.total_balance}")

    def check_total_loan_amount(self, bank):
        bank.total_loan_amount()

    def toggle_loan_feature(self, bank):
        bank.toggle_loan_feature()