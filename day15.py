class BankAccount():
    def __init__(self,name ):
        self.name=name
        self.balance=0.0
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        if self.balance<=0.0:
            return "insufficient balance"
        else:
            self.balance=self.balance-amount
        return self.balance
    def balances(self):
        output={
            "acc name":self.name,
            "current balance":self.balance
        }
        return output
    
obj=BankAccount("Ishani")
# obj.deposit(700)
print(obj.withdraw(100))
print(obj.balances())
