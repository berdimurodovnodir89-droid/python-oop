class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def show_balance(self):
        print(self.balance)
    def get_balance(self):
        return self.balance
acounts = [
    BankAccount('Nodirbek',10000),
    BankAccount('Jamol',100000),
    BankAccount('Vali',20000),
    BankAccount('Soli',350000),
    BankAccount('Nabi',2300000)
]
total = 0
for acount in acounts:
   total += acount.get_balance()
print(total)