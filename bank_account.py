class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance


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
        self.int_rate = 0.01
        self.balance = self.balance * self.int_rate + self.balance
        return self

account1 = BankAccount(100)
# account1.deposit(50)
# account1.withdraw(150)
# print(account1.balance)
# account1.display_account_info()
# account1.deposit(100)
# account1.yield_interest()
# account1.display_account_info()
account1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()