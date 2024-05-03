class Bank:
    def __init__(self):
        self.customers = []
        self.admins = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = True

    def find_account(self, account_number):
        for customer in self.customers:
            if customer.account_number == account_number:
                return customer
        return None

    def deposit(self, customer, amount):
        customer.balance += amount
        self.total_balance += amount
        customer.transactions.append(f"Deposited {amount}")
        print("Deposit successful")

    def withdraw(self, customer, amount):
        if amount > customer.balance:
            print("Withdrawal amount exceeded")
        else:
            customer.balance -= amount
            self.total_balance -= amount
            customer.transactions.append(f"Withdrawn {amount}")
            print("Withdrawal successful")

    def all_user_list(self):
        print("All Accounts:")
        for customer in self.customers:
            print(f"Name: {customer.name}, Account Number: {customer.account_number}, Account Type: {customer.account_type}")

    def total_loan_amount(self):
        total_loan = self.total_loan
        print(f"Total loan amount: {total_loan}")

    def toggle_loan_feature(self):
        self.loan_status = not self.loan_status
        if self.loan_status:
            print("Loan feature is on")
        else:
            print("Loan feature is off")