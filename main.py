import os
from bank import Bank
from users import Customer, Admin
            
Sonali_bank = Bank()

def customer_choice():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phone = int(input("Enter your phone: "))
    address = input("Enter your address: ")
    account_type = input("Enter account type: ")

    customer = Customer(name, age, phone, address, account_type)
    Sonali_bank.customers.append(customer)
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(f"Welcome {customer.name}!!!\n")
        print("Choose any of the options from below: ")
        print("1 : Deposit amount")
        print("2 : Withdraw amount")
        print("3 : Available Balance")
        print("4 : Transaction History")
        print("5 : Take Loan")
        print("6 : Transfer Money")
        print("7 : Exit")

        inputt = int(input("Enter the option: "))
        if inputt == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            amount = int(input("Enter the amount to deposit: "))
            customer.deposit(Sonali_bank, amount)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            amount = int(input("Enter amount: "))
            customer.withdraw(Sonali_bank, amount)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            customer.show_balance()
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            customer.transaction_history()
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            customer.take_loan(Sonali_bank)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            to_acc_no= int(input("Enter transfer account number: "))
            amount = int(input("Enter amount: "))
            customer.transfer_money(Sonali_bank, to_acc_no, amount)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input")
            print("----x------x------x----")
            print("----x------x------x----")

def admin_choice():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    phone = int(input("Enter your phone: "))
    address = input("Enter your address: ")

    admin = Admin(name, age, phone, address)
    Sonali_bank.admins.append(admin)
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(f"Welcome {admin.name}!!!\n")
        print("Choose any of the options from below: ")
        print("1 : Create Account")
        print("2 : Delete Account")
        print("3 : All User Account")
        print("4 : Total Balance")
        print("5 : Total Loan Amount")
        print("6 : On/OFF Loan")
        print("7 : Exit")

        inputt = int(input("Enter the option: "))
        if inputt == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            phone = int(input("Enter your phone: "))
            address = input("Enter your address: ")
            account_type = input("Enter account type: ")

            customer = Customer(name, age, phone, address, account_type)
            admin.create_account(Sonali_bank, customer)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            account_number = int(input("Enter account number: "))
            admin.delete_account(Sonali_bank, account_number)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            admin.all_user_list(Sonali_bank)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            admin.total_balance(Sonali_bank)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            admin.check_total_loan_amount(Sonali_bank)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            admin.toggle_loan_feature(Sonali_bank)
            print("----x------x------x----")
            print("----x------x------x----")
        elif inputt == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid input")
            print("----x------x------x----")
            print("----x------x------x----")

while True:
   print("Welcome!!! Choose any option from below")
   print("1. Admin")
   print("2. Customer")
   print("3. Exit")
   inputt = int(input("Enter your choice: "))
   if inputt == 1:
       os.system('cls' if os.name == 'nt' else 'clear')
       admin_choice()
   elif inputt == 2:
       os.system('cls' if os.name == 'nt' else 'clear')
       customer_choice()
   elif inputt == 3:
       os.system('cls' if os.name == 'nt' else 'clear')
       break
   else:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("Invalid input")
       print("----x------x------x----")
       print("----x------x------x----")