class User:
    def __init__(self):
        self.account = BankAccount (int_rate=0.01, balance=0)
        self.name = ""
    def depo(self, amount):
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_user_balance(self, display):
        self.account.balance = display
        return self


class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount 
        return self
        
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Balance: $", self.balance)
        return self
        
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self


nina = User()
liam = User()
andrew = User()

nina.account.deposit(100).display_account_info()