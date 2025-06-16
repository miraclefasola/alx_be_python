class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, deposit_amount):

        if deposit_amount <= 0:
            return "input an invalid amount"
        self.account_balance += deposit_amount
        return deposit_amount


    def withdraw(self, withdraw_amount):

        if withdraw_amount > self.account_balance:
            return False
        self.account_balance -= withdraw_amount
        return True
    def display_balance(self):
        print (f"Current Balance: ${self.account_balance:.2f}")