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
    def show_balance(self):
        print(f"Balance : {self.balance}")

balance1 = BankAccount('Nodirbek',10000)
balance2 = BankAccount('Jamol',100000)
balance3 = BankAccount('Vali',20000)


balance1.deposit(10000)
balance1.withdraw(5000)
balance1.withdraw(50000)
balance1.show_balance()
