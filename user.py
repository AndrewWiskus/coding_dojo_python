class User:
    def __init__(self, username):
        self.name = username
        self.balance = 100
    def make_deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount 
        print(nina.balance)
        return self
    def make_withdrawal(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        print(self.balance)
        return self
    def display_user_balance(self):
        print(self.balance)
        return self

nina = User("Nina")
liam = User("Liam")
andrew = User("Andrew")

# print(nina.make_deposit(100).make_deposit(200).make_deposit(300))
# print(liam.make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(50))
print(andrew.make_deposit(1000).make_withdrawal(57.02).make_withdrawal(13.91).make_withdrawal(14.70))
