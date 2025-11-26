class BankAccount:

    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance is {self.account_balance}.")
        else:
            print ("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds for this withdrawal.")
            return False
        elif amount <=0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            print(f"Withdrew {amount}. New balance is {self.account_balance}.")
            return True

    def display_balance(self):
        print(f"Current balance is {self.account_balance}.")

        