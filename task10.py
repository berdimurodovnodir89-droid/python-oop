class BankAccount:
    def __init__(self,owner,balance):
        self.own = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"yangi balance {self.balance}")
    def withdraw(self,amount):
        if amount <= self.balance :
            self.balance -= amount
            print(f"yangi balance {self.balance}")
        else :
            print('Balanc yetarli emas')

balance = BankAccount('Nodirbek',10000)


balance.deposit(10000)
balance.withdraw(5000)
balance.withdraw(50000)
